import numpy as np
import pandas as pd

from private_signals.experiments import (
    Experiment, assign_verdicts, cross_sectional_sort, tercile_spreads, walk_forward_sort,
)


def _toy_panel(n_quarters=24, n_sectors=9, seed=0, signal=0.0):
    rng = np.random.default_rng(seed)
    rows = []
    for q in pd.period_range("2018Q1", periods=n_quarters, freq="Q"):
        for s in range(n_sectors):
            f = rng.normal()
            rows.append({"quarter": q, "sector": f"s{s}", "funding_growth_qoq": f,
                         "fwd_1q": signal * f + rng.normal(scale=0.05),
                         "fwd_2q": signal * f + rng.normal(scale=0.07),
                         "fwd_4q": signal * f + rng.normal(scale=0.10)})
    p = pd.DataFrame(rows)
    p.attrs.update({"synthetic": True, "mode": "raw", "lag": 0})
    return p


def test_tercile_spreads_uses_floor_third_and_correct_sign():
    p = _toy_panel(n_quarters=1, n_sectors=9)
    q = p["quarter"].iloc[0]
    # make returns exactly the feature so top third mean > bottom third mean
    p["fwd_1q"] = p["funding_growth_qoq"]
    sp = tercile_spreads(p, "funding_growth_qoq", 1)
    g = p.sort_values("funding_growth_qoq")
    assert sp.loc[q, "k"] == 3
    expected = g["fwd_1q"].iloc[-3:].mean() - g["fwd_1q"].iloc[:3].mean()
    np.testing.assert_allclose(sp.loc[q, "spread"], expected)
    assert sp.loc[q, "spread"] > 0


def test_tercile_spreads_skips_thin_quarters():
    p = _toy_panel(n_quarters=3, n_sectors=5)
    assert tercile_spreads(p, "funding_growth_qoq", 1).empty


def test_sort_is_null_without_signal_and_detects_a_planted_one():
    null = cross_sectional_sort(_toy_panel(signal=0.0), "funding_growth_qoq", 1, "S1", n_boot=500, n_perm=300)
    assert null.pvalue > 0.05
    strong = cross_sectional_sort(_toy_panel(signal=0.10), "funding_growth_qoq", 1, "S2", n_boot=500, n_perm=300)
    assert strong.estimate > 0 and strong.ci_excludes_zero and strong.pvalue < 0.01


def test_walk_forward_folds_are_disjoint_and_cover_the_tail():
    s = cross_sectional_sort(_toy_panel(n_quarters=30), "funding_growth_qoq", 2, "S", n_boot=200, n_perm=50)
    w = walk_forward_sort(s, "W", n_splits=3, n_boot=200)
    folds = w.extra["folds"]
    assert len(folds) == 3 and folds["n_test"].sum() == w.n
    assert w.pvalue is None and "Descriptive" in w.verdict


def test_assign_verdicts_applies_bh_per_family():
    def mk(i, fam, p, lo, hi):
        return Experiment(id=f"{fam}{i}", family=fam, name="", feature="f", horizon=1, protocol="",
                          data="", n=10, estimate=(lo + hi) / 2, ci_low=lo, ci_high=hi, pvalue=p)
    exps = [mk(1, "a", 0.001, 0.1, 0.3), mk(2, "a", 0.04, 0.01, 0.5), mk(3, "a", 0.9, -0.2, 0.2),
            mk(1, "b", 0.04, 0.05, 0.4), mk(2, "b", 0.9, -0.1, 0.1)]
    assign_verdicts(exps, q=0.05)
    assert exps[0].verdict.startswith("Survives")
    assert exps[1].verdict.startswith("Nominally")       # 0.04*3/2 = 0.06 > 0.05
    assert exps[2].verdict.startswith("Null")
    assert exps[3].verdict.startswith("Nominally")       # 0.04*2/1 = 0.08 in its own family
    assert exps[4].p_adj == 0.9
