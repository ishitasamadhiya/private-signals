"""Statistics utilities, implemented from scratch with standard methodology.

* percentile bootstrap confidence intervals (i.i.d. and paired/cluster)
* permutation p-values (optionally restricted within clusters)
* Benjamini-Hochberg step-up false-discovery-rate control
* expanding-window walk-forward splits

Every randomised routine takes an explicit ``seed`` and defaults to 0 so that
every number in the ledger is reproducible.
"""
from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
from scipy.stats import rankdata


@dataclass
class BootstrapResult:
    estimate: float
    ci_low: float
    ci_high: float
    n: int
    n_boot: int
    alpha: float
    seed: int
    samples: np.ndarray = field(repr=False, default=None)

    @property
    def excludes_zero(self) -> bool:
        return self.ci_low > 0 or self.ci_high < 0


def _percentile_ci(samples: np.ndarray, alpha: float) -> tuple[float, float]:
    lo, hi = np.percentile(samples, [100 * alpha / 2, 100 * (1 - alpha / 2)])
    return float(lo), float(hi)


def bootstrap_ci(x, stat=np.mean, n_boot: int = 10_000, alpha: float = 0.05,
                 seed: int = 0) -> BootstrapResult:
    """Percentile bootstrap CI for ``stat(x)`` under i.i.d. resampling of ``x``.

    ``stat`` is called on each resample. For ``np.mean`` the loop is
    vectorised; other statistics are evaluated one resample at a time.
    """
    x = np.asarray(x, dtype=float)
    x = x[~np.isnan(x)]
    n = len(x)
    if n < 2:
        raise ValueError("need at least two observations")
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, n, size=(n_boot, n))
    if stat is np.mean:
        samples = x[idx].mean(axis=1)
    else:
        samples = np.array([stat(x[row]) for row in idx])
    lo, hi = _percentile_ci(samples, alpha)
    return BootstrapResult(float(stat(x)), lo, hi, n, n_boot, alpha, seed, samples)


def paired_bootstrap_ci(a, b, n_boot: int = 10_000, alpha: float = 0.05,
                        seed: int = 0) -> BootstrapResult:
    """Percentile bootstrap CI for ``mean(a - b)`` resampling *pairs* jointly.

    ``a`` and ``b`` must be aligned (same length, same units). Pairs with a
    NaN in either element are dropped. Resampling pairs rather than each array
    independently preserves whatever dependence exists within a pair, which is
    the right thing for e.g. top-tercile vs bottom-tercile returns measured in
    the same quarter.
    """
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    if a.shape != b.shape:
        raise ValueError("a and b must be aligned")
    keep = ~(np.isnan(a) | np.isnan(b))
    d = a[keep] - b[keep]
    n = len(d)
    if n < 2:
        raise ValueError("need at least two complete pairs")
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, n, size=(n_boot, n))
    samples = d[idx].mean(axis=1)
    lo, hi = _percentile_ci(samples, alpha)
    return BootstrapResult(float(d.mean()), lo, hi, n, n_boot, alpha, seed, samples)


def cluster_bootstrap_ci(clusters, stat, n_boot: int = 10_000, alpha: float = 0.05,
                         seed: int = 0) -> BootstrapResult:
    """Percentile bootstrap CI resampling whole clusters with replacement.

    ``clusters`` is a sequence of array-like blocks (e.g. one 2-D array of
    (x, y) rows per quarter). Each bootstrap draw samples ``len(clusters)``
    clusters with replacement, concatenates them, and evaluates ``stat`` on the
    stacked array. Use this when observations within a cluster are dependent
    (all sectors in the same quarter share common shocks).
    """
    blocks = [np.asarray(c) for c in clusters if len(c) > 0]
    k = len(blocks)
    if k < 2:
        raise ValueError("need at least two clusters")
    rng = np.random.default_rng(seed)
    samples = np.empty(n_boot)
    for i in range(n_boot):
        pick = rng.integers(0, k, size=k)
        samples[i] = stat(np.concatenate([blocks[j] for j in pick], axis=0))
    full = np.concatenate(blocks, axis=0)
    lo, hi = _percentile_ci(samples, alpha)
    return BootstrapResult(float(stat(full)), lo, hi, len(full), n_boot, alpha, seed, samples)


def spearman(x, y) -> float:
    """Spearman rank correlation with average ranks for ties."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    if len(x) != len(y) or len(x) < 3:
        return float("nan")
    rx = rankdata(x)
    ry = rankdata(y)
    rx = rx - rx.mean()
    ry = ry - ry.mean()
    denom = np.sqrt((rx ** 2).sum() * (ry ** 2).sum())
    if denom == 0:
        return float("nan")
    return float((rx * ry).sum() / denom)


def permutation_pvalue(x, y, stat, n_perm: int = 10_000, seed: int = 0,
                       groups=None) -> tuple[float, float]:
    """Two-sided permutation p-value for ``stat(x, y)`` under H0: x independent of y.

    ``y`` is shuffled; when ``groups`` is given, shuffling happens only within
    each group (e.g. within a quarter) so that common group-level shocks are
    preserved under the null. Returns ``(observed_stat, p_value)`` with the
    standard ``(k + 1) / (n_perm + 1)`` correction so p is never exactly 0.
    """
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    rng = np.random.default_rng(seed)
    observed = stat(x, y)
    if groups is None:
        group_idx = [np.arange(len(y))]
    else:
        groups = np.asarray(groups)
        group_idx = [np.flatnonzero(groups == g) for g in np.unique(groups)]
    y_perm = y.copy()
    count = 0
    for _ in range(n_perm):
        for idx in group_idx:
            y_perm[idx] = y[idx][rng.permutation(len(idx))]
        if abs(stat(x, y_perm)) >= abs(observed):
            count += 1
    return float(observed), (count + 1) / (n_perm + 1)


def benjamini_hochberg(pvalues, q: float = 0.05) -> tuple[np.ndarray, np.ndarray]:
    """Benjamini-Hochberg step-up procedure.

    Returns ``(reject, p_adjusted)`` where ``reject[i]`` is True when hypothesis
    ``i`` is rejected at FDR level ``q`` and ``p_adjusted`` are the BH-adjusted
    p-values (monotone, capped at 1). NaN p-values are ignored and returned as
    NaN / not rejected.
    """
    p = np.asarray(pvalues, dtype=float)
    reject = np.zeros(p.shape, dtype=bool)
    p_adj = np.full(p.shape, np.nan)
    valid = ~np.isnan(p)
    m = int(valid.sum())
    if m == 0:
        return reject, p_adj
    pv = p[valid]
    order = np.argsort(pv)
    ranks = np.arange(1, m + 1)
    adj_sorted = pv[order] * m / ranks
    # enforce monotonicity from the largest rank downwards
    adj_sorted = np.minimum.accumulate(adj_sorted[::-1])[::-1]
    adj_sorted = np.minimum(adj_sorted, 1.0)
    adj = np.empty(m)
    adj[order] = adj_sorted
    p_adj[valid] = adj
    reject[valid] = adj <= q
    return reject, p_adj


def walk_forward_splits(periods, n_splits: int = 4, min_train_frac: float = 0.4):
    """Expanding-window walk-forward splits over an ordered sequence of periods.

    The first ``min_train_frac`` of periods is the initial training window; the
    remainder is cut into ``n_splits`` contiguous test blocks. Each split trains
    on everything before its test block. Returns a list of
    ``(train_periods, test_periods)`` tuples.
    """
    periods = list(periods)
    n = len(periods)
    n_train0 = int(round(n * min_train_frac))
    n_test_total = n - n_train0
    if n_splits < 1 or n_test_total < n_splits:
        raise ValueError("not enough periods for the requested splits")
    edges = np.linspace(n_train0, n, n_splits + 1).round().astype(int)
    splits = []
    for a, b in zip(edges[:-1], edges[1:]):
        splits.append((periods[:a], periods[a:b]))
    return splits
