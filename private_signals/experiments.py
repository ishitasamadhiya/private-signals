"""The experiments. Each returns an ``Experiment`` record for the ledger.

Families for multiple-testing correction (Benjamini-Hochberg, q = 0.05):

* ``sorts``      cross-sectional top-third minus bottom-third spreads,
                 one test per (feature, horizon)
* ``pooled``     pooled Spearman rank correlations, one per (feature, horizon)
* ``by_sector``  per-sector time-series Spearman for the primary feature,
                 one per (sector, horizon)

Robustness re-runs of the primary sort (other return modes, lag = 1) are
reported but deliberately kept *out* of the BH families: they are variations
of the same hypothesis, not independent hypotheses, and listing them as extra
tests would make the correction look stricter than it is.
"""
from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import pandas as pd

from .stats import (
    benjamini_hochberg,
    block_bootstrap_ci,
    cluster_bootstrap_ci,
    permutation_pvalue,
    spearman,
    walk_forward_splits,
)

PRIMARY_FEATURE = "funding_growth_qoq"
Q_FDR = 0.05


@dataclass
class Experiment:
    id: str
    family: str
    name: str
    feature: str
    horizon: int
    protocol: str
    data: str
    n: int
    estimate: float
    ci_low: float
    ci_high: float
    pvalue: float | None
    p_adj: float | None = None
    verdict: str = ""
    notes: list[str] = field(default_factory=list)
    extra: dict = field(default_factory=dict, repr=False)

    @property
    def ci_excludes_zero(self) -> bool:
        return self.ci_low > 0 or self.ci_high < 0


def assign_verdicts(experiments: list[Experiment], q: float = Q_FDR) -> None:
    """Apply BH within each family, then write a plain-language verdict on each record."""
    for fam in sorted({e.family for e in experiments}):
        fam_exps = [e for e in experiments if e.family == fam and e.pvalue is not None]
        if not fam_exps:
            continue
        reject, p_adj = benjamini_hochberg([e.pvalue for e in fam_exps], q=q)
        for e, r, pa in zip(fam_exps, reject, p_adj):
            e.p_adj = float(pa)
            if r and e.ci_excludes_zero:
                e.verdict = (f"Survives BH at q={q} within the '{fam}' family and the 95% CI excludes 0. "
                             "Treat as a lead to replicate out of sample, not as a finding.")
            elif e.pvalue <= 0.05 or e.ci_excludes_zero:
                e.verdict = ("Nominally significant but does NOT survive BH correction (or the CI and the "
                             "permutation test disagree). No claim.")
            else:
                e.verdict = "Null: no evidence of an effect at this horizon."
    for e in experiments:
        if e.pvalue is None and not e.verdict:
            e.verdict = "Descriptive only (no hypothesis test)."


# ----------------------------------------------------------------------------
# helpers
# ----------------------------------------------------------------------------

def _describe(panel: pd.DataFrame, df: pd.DataFrame) -> str:
    src = "SYNTHETIC fixture (FAKE data)" if panel.attrs.get("synthetic") else "PitchBook export"
    return (f"{src}; returns={panel.attrs.get('mode')}, lag={panel.attrs.get('lag')}q; "
            f"{df['quarter'].min()}..{df['quarter'].max()}, {df['sector'].nunique()} sectors, "
            f"{len(df)} sector-quarters")


# ----------------------------------------------------------------------------
# 1. pooled rank correlation
# ----------------------------------------------------------------------------

def pooled_rank_correlation(panel: pd.DataFrame, feature: str, horizon: int, exp_id: str,
                            n_boot: int = 10_000, n_perm: int = 5_000, seed: int = 0) -> Experiment:
    """Spearman(feature_t, fwd return_{t..t+h}) pooled over all sector-quarters.

    CI: cluster bootstrap resampling *quarters* (all sectors in a quarter move
    together). p-value: permutation of returns *within* each quarter, which
    preserves quarter-level common shocks under the null.
    """
    col = f"fwd_{horizon}q"
    df = panel[["quarter", "sector", feature, col]].dropna()
    x, y = df[feature].to_numpy(), df[col].to_numpy()
    clusters = [g[[feature, col]].to_numpy() for _, g in df.groupby("quarter")]
    boot = cluster_bootstrap_ci(clusters, lambda a: spearman(a[:, 0], a[:, 1]),
                                n_boot=n_boot, seed=seed)
    _, p = permutation_pvalue(x, y, spearman, n_perm=n_perm, seed=seed,
                              groups=df["quarter"].astype(str).to_numpy())
    return Experiment(
        id=exp_id, family="pooled", name="Pooled Spearman rank correlation",
        feature=feature, horizon=horizon,
        protocol=(f"Spearman rho between {feature} in quarter t and the {horizon}Q forward return "
                  f"from the end of t (+lag), pooled over sector-quarters. 95% CI: percentile "
                  f"cluster bootstrap over quarters ({n_boot:,} resamples, seed {seed}). Two-sided "
                  f"p: permutation of returns within quarter ({n_perm:,} permutations)."),
        data=_describe(panel, df), n=len(df),
        estimate=boot.estimate, ci_low=boot.ci_low, ci_high=boot.ci_high, pvalue=p,
        notes=[f"{len(clusters)} quarter clusters."],
    )


# ----------------------------------------------------------------------------
# 2. cross-sectional tercile sort
# ----------------------------------------------------------------------------

def tercile_spreads(panel: pd.DataFrame, feature: str, horizon: int,
                    min_sectors: int = 6) -> pd.DataFrame:
    """Per quarter: mean forward return of the top third of sectors by ``feature``
    minus the bottom third. Returns a DataFrame indexed by quarter with columns
    ``top, bottom, spread, k, n``."""
    col = f"fwd_{horizon}q"
    rows = []
    for q, g in panel[["quarter", "sector", feature, col]].dropna().groupby("quarter"):
        n = len(g)
        if n < min_sectors:
            continue
        k = n // 3
        g = g.sort_values(feature)
        bottom = g[col].iloc[:k].mean()
        top = g[col].iloc[-k:].mean()
        rows.append({"quarter": q, "top": top, "bottom": bottom, "spread": top - bottom, "k": k, "n": n})
    cols = ["quarter", "top", "bottom", "spread", "k", "n"]
    return pd.DataFrame(rows, columns=cols).set_index("quarter")


def _sort_permutation_pvalue(panel, feature, horizon, observed, n_perm, seed, min_sectors=6) -> float:
    """Shuffle returns within each quarter, recompute the mean tercile spread."""
    col = f"fwd_{horizon}q"
    groups = []
    for _, g in panel[["quarter", feature, col]].dropna().groupby("quarter"):
        n = len(g)
        if n < min_sectors:
            continue
        groups.append((g[col].to_numpy(), n // 3))
    rng = np.random.default_rng(seed)
    count = 0
    for _ in range(n_perm):
        spreads = np.empty(len(groups))
        for i, (r, k) in enumerate(groups):
            rp = r[rng.permutation(len(r))]
            spreads[i] = rp[-k:].mean() - rp[:k].mean()
        if abs(spreads.mean()) >= abs(observed):
            count += 1
    return (count + 1) / (n_perm + 1)


def cross_sectional_sort(panel: pd.DataFrame, feature: str, horizon: int, exp_id: str,
                         n_boot: int = 10_000, n_perm: int = 5_000, seed: int = 0,
                         family: str = "sorts") -> Experiment:
    """Top-third minus bottom-third forward return, averaged over quarters.

    CI: paired by quarter (top and bottom are measured in the same quarter), so
    the statistic is the mean of the per-quarter spread series; resampled with a
    circular block bootstrap whose block length equals the horizon, because
    h-quarter forward windows overlap for consecutive signal quarters.
    """
    sp = tercile_spreads(panel, feature, horizon)
    boot = block_bootstrap_ci(sp["spread"].to_numpy(), block_len=horizon, n_boot=n_boot, seed=seed)
    p = _sort_permutation_pvalue(panel, feature, horizon, boot.estimate, n_perm, seed)
    df = panel[["quarter", "sector", feature, f"fwd_{horizon}q"]].dropna()
    unit = "sigma" if panel.attrs.get("mode") == "vol_adj" else "return"
    return Experiment(
        id=exp_id, family=family, name="Cross-sectional tercile sort (top third minus bottom third)",
        feature=feature, horizon=horizon,
        protocol=(f"Each quarter rank sectors by {feature}; long the top third, short the bottom "
                  f"third (k = n//3, min 6 sectors); hold {horizon}Q. Statistic: mean quarterly spread "
                  f"({unit}). 95% CI: paired-by-quarter circular block bootstrap, block = {horizon} "
                  f"quarters ({n_boot:,} resamples, seed {seed}). Two-sided p: within-quarter "
                  f"permutation of returns ({n_perm:,} permutations)."),
        data=_describe(panel, df), n=len(sp),
        estimate=boot.estimate, ci_low=boot.ci_low, ci_high=boot.ci_high, pvalue=p,
        notes=[f"Mean top-third {unit} {sp['top'].mean():+.4f}, bottom-third {sp['bottom'].mean():+.4f}; "
               f"hit rate (spread > 0) {(sp['spread'] > 0).mean():.0%} of {len(sp)} quarters."],
        extra={"spreads": sp},
    )


# ----------------------------------------------------------------------------
# 3. walk-forward
# ----------------------------------------------------------------------------

def walk_forward_sort(sort_exp: Experiment, exp_id: str, n_splits: int = 4, n_boot: int = 10_000,
                      seed: int = 0) -> Experiment:
    """Does the sign of the tercile spread learned in-sample persist out of sample?

    Expanding-window splits over quarters. For each fold, the in-sample
    direction is sign(mean train spread); the fold "agrees" if the mean test
    spread has the same sign. The headline statistic is the mean out-of-sample
    spread across all folds (with a block bootstrap CI); this is descriptive
    and is not entered into a BH family.
    """
    sp = sort_exp.extra["spreads"]["spread"]
    splits = walk_forward_splits(list(sp.index), n_splits=n_splits)
    folds = []
    for i, (train, test) in enumerate(splits, 1):
        tr, te = sp.loc[train].mean(), sp.loc[test].mean()
        folds.append({"fold": i, "train_end": str(train[-1]), "test_start": str(test[0]),
                      "test_end": str(test[-1]), "n_test": len(test), "train_mean": tr,
                      "test_mean": te, "agrees": bool(np.sign(tr) == np.sign(te))})
    folds = pd.DataFrame(folds)
    oos = sp.loc[[q for _, test in splits for q in test]].to_numpy()
    boot = block_bootstrap_ci(oos, block_len=sort_exp.horizon, n_boot=n_boot, seed=seed)
    agree = int(folds["agrees"].sum())
    return Experiment(
        id=exp_id, family="walk_forward", name="Walk-forward sign persistence of the tercile spread",
        feature=sort_exp.feature, horizon=sort_exp.horizon,
        protocol=(f"Expanding-window walk-forward with {n_splits} test folds over the quarterly spread "
                  f"series from {sort_exp.id}; first 40% of quarters is the initial training window. "
                  f"Report per-fold train/test mean spread and sign agreement, plus the pooled OOS mean "
                  f"with a block bootstrap CI (block = {sort_exp.horizon}, {n_boot:,} resamples, seed {seed})."),
        data=sort_exp.data, n=len(oos),
        estimate=boot.estimate, ci_low=boot.ci_low, ci_high=boot.ci_high, pvalue=None,
        verdict=(f"Sign agreement in {agree}/{n_splits} folds. "
                 + ("OOS CI excludes 0." if boot.excludes_zero else "OOS CI includes 0.")
                 + " Descriptive: no hypothesis test entered into BH."),
        notes=[f"Fold {r.fold}: train to {r.train_end} mean {r.train_mean:+.4f}; test {r.test_start}..{r.test_end} "
               f"(n={r.n_test}) mean {r.test_mean:+.4f}; {'agree' if r.agrees else 'DISAGREE'}"
               for r in folds.itertuples()],
        extra={"folds": folds},
    )


# ----------------------------------------------------------------------------
# 4. per-sector time-series rank correlation
# ----------------------------------------------------------------------------

def per_sector_rank_correlation(panel: pd.DataFrame, feature: str, horizons, id_prefix: str,
                                n_perm: int = 5_000, seed: int = 0) -> list[Experiment]:
    """Within each sector: Spearman between the feature and the forward return over time.

    p-values are from an unrestricted time-permutation, which ignores serial
    dependence from overlapping windows and therefore understates p at the 2Q
    and 4Q horizons. That bias is *against* the null, so a null here is
    conservative; a rejection here is not, and should be read with that in mind.
    """
    out = []
    i = 0
    for sector, g in panel.groupby("sector"):
        for h in horizons:
            col = f"fwd_{h}q"
            d = g[[feature, col]].dropna()
            i += 1
            if len(d) < 12:
                continue
            rho, p = permutation_pvalue(d[feature].to_numpy(), d[col].to_numpy(), spearman,
                                        n_perm=n_perm, seed=seed)
            out.append(Experiment(
                id=f"{id_prefix}-{sector}-{h}q", family="by_sector",
                name=f"Per-sector Spearman ({sector})", feature=feature, horizon=h,
                protocol=(f"Spearman rho over time between {feature} and the {h}Q forward return within "
                          f"sector '{sector}'. Two-sided p: unrestricted permutation ({n_perm:,}, seed {seed}); "
                          f"no CI reported (n small; the BH-adjusted p is the decision statistic)."),
                data=_describe(panel, panel[panel.sector == sector].dropna(subset=[feature, col])),
                n=len(d), estimate=rho, ci_low=float("nan"), ci_high=float("nan"), pvalue=p,
                notes=["Time-permutation p ignores overlap at h>1: anti-conservative."] if h > 1 else [],
            ))
    return out
