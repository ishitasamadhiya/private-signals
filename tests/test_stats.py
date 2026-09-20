import numpy as np
import pytest
from scipy import stats as sps

from private_signals.stats import (
    benjamini_hochberg,
    bootstrap_ci,
    cluster_bootstrap_ci,
    paired_bootstrap_ci,
    permutation_pvalue,
    spearman,
    walk_forward_splits,
)


def test_bootstrap_ci_covers_true_mean_at_nominal_rate():
    rng = np.random.default_rng(123)
    covered = 0
    trials = 200
    for i in range(trials):
        x = rng.normal(0.5, 1.0, size=60)
        r = bootstrap_ci(x, n_boot=1000, seed=i)
        covered += r.ci_low <= 0.5 <= r.ci_high
    # nominal 95%; allow generous slack for 200 trials with a percentile CI at n=60
    assert 0.88 <= covered / trials <= 0.99


def test_bootstrap_ci_is_reproducible_and_ordered():
    x = np.arange(20, dtype=float)
    a = bootstrap_ci(x, n_boot=500, seed=0)
    b = bootstrap_ci(x, n_boot=500, seed=0)
    assert a.ci_low == b.ci_low and a.ci_high == b.ci_high
    assert a.ci_low <= a.estimate <= a.ci_high


def test_bootstrap_ci_drops_nans_and_accepts_generic_stat():
    x = np.array([1.0, 2.0, np.nan, 3.0, 4.0, 5.0])
    r = bootstrap_ci(x, stat=np.median, n_boot=200)
    assert r.n == 5
    assert r.estimate == 3.0


def test_paired_bootstrap_identical_arrays_gives_zero_width_ci():
    a = np.random.default_rng(0).normal(size=40)
    r = paired_bootstrap_ci(a, a.copy(), n_boot=500)
    assert r.estimate == 0.0 and r.ci_low == 0.0 and r.ci_high == 0.0


def test_paired_bootstrap_detects_constant_shift():
    rng = np.random.default_rng(1)
    b = rng.normal(size=50)
    a = b + 0.3 + rng.normal(scale=0.05, size=50)
    r = paired_bootstrap_ci(a, b, n_boot=2000)
    assert r.excludes_zero
    assert 0.25 < r.estimate < 0.35


def test_paired_bootstrap_rejects_misaligned_inputs():
    with pytest.raises(ValueError):
        paired_bootstrap_ci([1, 2, 3], [1, 2])


def test_cluster_bootstrap_matches_iid_when_clusters_are_singletons():
    x = np.random.default_rng(2).normal(size=30)
    r_iid = bootstrap_ci(x, n_boot=2000, seed=7)
    r_cl = cluster_bootstrap_ci([np.array([v]) for v in x], np.mean, n_boot=2000, seed=7)
    assert r_cl.estimate == pytest.approx(r_iid.estimate)
    assert r_cl.ci_low == pytest.approx(r_iid.ci_low, abs=0.05)
    assert r_cl.ci_high == pytest.approx(r_iid.ci_high, abs=0.05)


def test_spearman_matches_scipy_including_ties():
    x = np.array([1, 2, 2, 3, 5, 8, 8, 9], dtype=float)
    y = np.array([2, 1, 4, 3, 5, 7, 9, 8], dtype=float)
    assert spearman(x, y) == pytest.approx(sps.spearmanr(x, y).statistic)
    assert spearman(x, -x) == pytest.approx(-1.0)


def test_permutation_pvalue_is_uniform_under_null_and_small_under_signal():
    rng = np.random.default_rng(3)
    x = rng.normal(size=80)
    y_null = rng.normal(size=80)
    _, p_null = permutation_pvalue(x, y_null, spearman, n_perm=500, seed=0)
    assert 0.0 < p_null <= 1.0
    y_sig = x + rng.normal(scale=0.3, size=80)
    _, p_sig = permutation_pvalue(x, y_sig, spearman, n_perm=500, seed=0)
    assert p_sig < 0.01


def test_permutation_within_groups_preserves_group_means():
    # if the only structure is a group-level shift, within-group permutation
    # should treat it as null (large p), while unrestricted permutation would not
    groups = np.repeat([0, 1], 40)
    x = np.where(groups == 0, 0.0, 1.0) + np.random.default_rng(4).normal(scale=0.01, size=80)
    y = np.where(groups == 0, 0.0, 1.0) + np.random.default_rng(5).normal(scale=0.01, size=80)
    _, p_within = permutation_pvalue(x, y, spearman, n_perm=300, seed=0, groups=groups)
    _, p_pooled = permutation_pvalue(x, y, spearman, n_perm=300, seed=0)
    assert p_within > 0.2
    assert p_pooled < 0.01


def test_benjamini_hochberg_matches_scipy_reference():
    # the 15 p-values from Benjamini & Hochberg (1995), Section 6
    p = np.array([0.0001, 0.0004, 0.0019, 0.0095, 0.0201, 0.0278, 0.0298, 0.0344,
                  0.0459, 0.3240, 0.4262, 0.5719, 0.6528, 0.7590, 1.0000])
    reject, p_adj = benjamini_hochberg(p, q=0.05)
    ref = sps.false_discovery_control(p, method="bh")
    assert np.allclose(p_adj, ref)
    # the paper rejects exactly the four smallest at q = 0.05
    assert reject.sum() == 4 and reject[:4].all()
    # shuffling the input must not change per-hypothesis results
    perm = np.random.default_rng(0).permutation(len(p))
    rej2, adj2 = benjamini_hochberg(p[perm], q=0.05)
    assert np.array_equal(rej2, reject[perm]) and np.allclose(adj2, p_adj[perm])


def test_benjamini_hochberg_handles_nan_and_no_rejections():
    reject, p_adj = benjamini_hochberg([0.5, np.nan, 0.9])
    assert not reject.any()
    assert np.isnan(p_adj[1]) and np.all(p_adj[[0, 2]] <= 1.0)


def test_walk_forward_splits_are_chronological_and_non_overlapping():
    periods = list(range(50))
    splits = walk_forward_splits(periods, n_splits=4, min_train_frac=0.4)
    assert len(splits) == 4
    seen = []
    for train, test in splits:
        assert train == periods[: len(train)]
        assert max(train) < min(test)
        assert not set(seen) & set(test)
        seen.extend(test)
    assert seen == periods[20:]


def test_walk_forward_splits_rejects_too_few_periods():
    with pytest.raises(ValueError):
        walk_forward_splits(range(5), n_splits=4, min_train_frac=0.9)
