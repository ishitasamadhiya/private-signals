# Private Signals

**Does private-market (VC / growth-equity) funding activity in a sector lead
public-market returns for that sector?**

A small, reproducible study built to be argued with. Every experiment has a
protocol, a confidence interval, a permutation p-value, a multiple-testing
correction, and a verdict, recorded in [`ledger.md`](ledger.md). A null result
is a valid outcome here and is reported as such.

> **Status: the committed ledger and figures were produced on a SYNTHETIC
> fixture (fake funding data).** They demonstrate that the pipeline runs end to
> end; they are not findings. Real results require a PitchBook export, which is
> licensed and is never committed (see [Data policy](#data-policy)).

## Question, made precise

For sector *s* and quarter *t*, let `funding_growth_qoq` be the change in log
total VC/growth funding from *t-1* to *t*. Let `fwd_hq` be the return of the
sector's ETF from the last trading day of *t* to the last trading day of *t+h*,
for *h* in {1, 2, 4} quarters, after removing beta times the SPY return
(beta estimated on trailing daily returns ending at *t*, so no look-ahead).

The hypothesis "private funding leads public returns" predicts that sectors
whose funding grew fastest in *t* out-perform, beta-neutral, over the next
*h* quarters. Two secondary features test the same idea with different
inputs: `deal_growth_qoq` (log deal count) and `funding_growth_yoy`.

## Design

| piece | choice | why |
|---|---|---|
| Public side | 10 sector ETFs + SPY, daily adjusted closes via yfinance, 2014 onward | liquid, investable proxies for sector returns |
| Private side | PitchBook sector x quarter export: total funding, deal count, median valuation | the standard source; loader in `private_signals/loader.py` |
| Sector map | `private_signals/sectors.py` | PitchBook verticals do not map 1:1 to ETFs; the mapping is explicit so it can be challenged |
| Returns | raw, beta-neutral excess (default), or vol-adjusted | isolates sector-specific return from the market factor |
| Timing | signal at end of quarter *t*, return from end of *t* (+ optional lag) | `--lag 1` is the robustness check for PitchBook's reporting delay |

### Experiments

1. **Cross-sectional tercile sorts** (`S01-S09`). Each quarter, rank sectors by
   the feature, take the top third minus the bottom third of forward returns,
   and average the spread over quarters. CI: paired-by-quarter circular
   **block bootstrap** with block length = horizon, because 2Q and 4Q forward
   windows overlap for consecutive quarters. p: permutation of returns
   *within* quarter, which preserves quarter-level common shocks.
2. **Pooled Spearman rank correlations** (`P01-P09`) between the feature and
   the forward return over all sector-quarters. CI: cluster bootstrap over
   quarters. p: within-quarter permutation.
3. **Per-sector time-series rank correlations** (`B-*`) for the primary
   feature, 10 sectors x 3 horizons. Decision statistic is the BH-adjusted p.
4. **Walk-forward** (`W01-W03`): expanding-window splits of the sort spread
   series; does the in-sample sign persist out of sample? Descriptive only.

Multiple testing: **Benjamini-Hochberg at q = 0.05 within each family**
(sorts: 9 tests; pooled: 9; per-sector: 30). Robustness re-runs with other
return modes or lags are variations of the same hypothesis and are kept out
of the families so the correction is not made to look stricter than it is.

All statistics utilities (`private_signals/stats.py`) are implemented from
scratch with standard methodology: percentile bootstrap (i.i.d., paired,
cluster, circular block), permutation tests, BH step-up, walk-forward splits.
Every randomised routine takes a seed (default 0). 10,000 bootstrap resamples
and 5,000 permutations per test; a full run takes about a minute.

## Findings

**On the synthetic fixture: 0 of 48 tests survive BH correction**, which is the
expected outcome for data with no planted relationship. The point of that run
is to show that the pipeline does not manufacture significance from noise.

Real findings will be written here after a PitchBook run. The pre-registered
reading rule: a result counts only if its 95% CI excludes zero **and** its
BH-adjusted p is at or below 0.05 **and** the walk-forward sign agrees in a
majority of folds. Anything short of that is reported as null or as "lead,
not finding".

Figures (`figures/`): `sort_spreads.png` (spread with CI per feature and
horizon), `cumulative_spread_{1,2,4}q.png` (cumulative spread with walk-forward
folds), `sector_rank_corr_heatmap.png`, `bh_pvalues.png` (sorted p-values
against the BH line, per family).

## Data policy

* **PitchBook data is never committed.** `data/` is git-ignored from the first
  commit; only `data/README.md` and the synthetic fixture are tracked. The
  derived `results/panel.csv` is git-ignored too, since it would contain
  PitchBook-derived features.
* `data/README.md` documents the exact columns the loader expects so anyone
  with their own PitchBook access can reproduce the study.
* `data/synthetic_fixture.csv` is **FAKE**: a seeded AR(1) process in logs with
  no relationship to real funding or returns. Its first line says so, the
  loader detects the marker, and every downstream artifact is watermarked
  `SYNTHETIC`.
* Market data comes from Yahoo Finance through `yfinance` and is cached under
  `cache/` (git-ignored).

## Reproduce

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python -m pytest -q                          # 36 tests
.venv/bin/python scripts/run_experiments.py            # fixture, or data/pitchbook_export.csv if present
.venv/bin/python scripts/run_experiments.py --mode raw --lag 1   # robustness variant
```

Outputs: `ledger.md`, `results/summary.csv`, `results/run_meta.json`, `figures/*.png`.

## Known limitations

* Ten sectors is a thin cross-section; terciles are three sectors each.
  Cross-sectional power is low by construction, which is why the ledger leans
  on CIs rather than on p-values alone.
* Per-sector time-series p-values use an unrestricted permutation that ignores
  the serial dependence induced by overlapping 2Q and 4Q windows. That bias is
  against the null, so a null there is conservative and a rejection is not.
* ETF inception dates (HACK late 2014, FINX late 2016) shorten the early
  cross-section.
* The sector-to-ETF mapping is a judgment call. It is isolated in one file so
  it can be varied.

## Layout

```
private_signals/
  sectors.py      sector -> ETF mapping
  loader.py       PitchBook CSV loader, synthetic detection, cached prices
  panel.py        forward returns (raw / excess / vol-adjusted), funding features, panel join
  stats.py        bootstrap, permutation, Benjamini-Hochberg, walk-forward (from scratch)
  experiments.py  the four experiments and verdict rules
  ledger.py       renders ledger.md
  figures.py      matplotlib figures
scripts/
  run_experiments.py, make_synthetic_fixture.py
tests/            pytest suites for stats, loader, panel, experiments
```
