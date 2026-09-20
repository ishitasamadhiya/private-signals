# Experiment ledger

> **WARNING: EVERY NUMBER BELOW WAS COMPUTED ON THE SYNTHETIC FIXTURE (FAKE DATA).**
> The private-funding side is a seeded random process with no relationship to real
> markets. This ledger exists to show the pipeline runs end to end. Nothing in it is a
> finding. Re-run with a PitchBook export (see `data/README.md`) to get real entries.

Generated 2026-09-19 at commit `ee7f81e` by `scripts/run_experiments.py`.

## Run configuration

| setting | value |
|---|---|
| synthetic | True |
| private_source | synthetic_fixture.csv |
| return_mode | excess |
| signal_lag_quarters | 0 |
| horizons_q | [1, 2, 4] |
| features | ['funding_growth_qoq', 'deal_growth_qoq', 'funding_growth_yoy'] |
| primary_feature | funding_growth_qoq |
| sectors | software->IGV, cybersecurity->HACK, biotech->XBI, semiconductors->SMH, fintech->FINX, technology->XLK, healthcare->XLV, financials->XLF, energy->XLE, industrials->XLI |
| market | SPY |
| price_sample | 2014-01-02..2026-09-18 |
| panel_quarters | 2014Q1..2026Q2 |
| n_boot | 10000 |
| n_perm | 5000 |
| seed | 0 |
| bh_q | 0.05 |

## Summary

| id | family | feature | h | n | estimate | 95% CI | p | BH p | verdict |
|---|---|---|---|---|---|---|---|---|---|
| S01 | sorts | funding_growth_qoq | 1Q | 47 | -0.0111 | [-0.0288, +0.0061] | 0.2733 | 0.7654 | Null: no evidence of an effect at this horizon |
| S02 | sorts | funding_growth_qoq | 2Q | 46 | +0.0003 | [-0.0221, +0.0229] | 0.9864 | 0.9864 | Null: no evidence of an effect at this horizon |
| S03 | sorts | funding_growth_qoq | 4Q | 44 | +0.0152 | [-0.0234, +0.0520] | 0.5103 | 0.7654 | Null: no evidence of an effect at this horizon |
| S04 | sorts | deal_growth_qoq | 1Q | 47 | -0.0006 | [-0.0248, +0.0217] | 0.9562 | 0.9864 | Null: no evidence of an effect at this horizon |
| S05 | sorts | deal_growth_qoq | 2Q | 46 | +0.0130 | [-0.0119, +0.0365] | 0.3957 | 0.7654 | Null: no evidence of an effect at this horizon |
| S06 | sorts | deal_growth_qoq | 4Q | 44 | +0.0320 | [+0.0036, +0.0609] | 0.1576 | 0.7654 | Nominally significant but does NOT survive BH correction (or the CI and the permutation test disagree) |
| S07 | sorts | funding_growth_yoy | 1Q | 45 | +0.0079 | [-0.0105, +0.0254] | 0.4503 | 0.7654 | Null: no evidence of an effect at this horizon |
| S08 | sorts | funding_growth_yoy | 2Q | 44 | +0.0176 | [-0.0139, +0.0503] | 0.2490 | 0.7654 | Null: no evidence of an effect at this horizon |
| S09 | sorts | funding_growth_yoy | 4Q | 42 | -0.0009 | [-0.0429, +0.0396] | 0.9632 | 0.9864 | Null: no evidence of an effect at this horizon |
| P01 | pooled | funding_growth_qoq | 1Q | 457 | -0.0090 | [-0.0997, +0.0783] | 0.8442 | 0.9292 | Null: no evidence of an effect at this horizon |
| P02 | pooled | funding_growth_qoq | 2Q | 447 | +0.0299 | [-0.0525, +0.1110] | 0.4925 | 0.7388 | Null: no evidence of an effect at this horizon |
| P03 | pooled | funding_growth_qoq | 4Q | 427 | +0.0535 | [-0.0410, +0.1457] | 0.2428 | 0.7283 | Null: no evidence of an effect at this horizon |
| P04 | pooled | deal_growth_qoq | 1Q | 457 | -0.0039 | [-0.1021, +0.0907] | 0.9292 | 0.9292 | Null: no evidence of an effect at this horizon |
| P05 | pooled | deal_growth_qoq | 2Q | 447 | +0.0317 | [-0.0533, +0.1226] | 0.4775 | 0.7388 | Null: no evidence of an effect at this horizon |
| P06 | pooled | deal_growth_qoq | 4Q | 427 | +0.0473 | [-0.0498, +0.1439] | 0.3333 | 0.7388 | Null: no evidence of an effect at this horizon |
| P07 | pooled | funding_growth_yoy | 1Q | 441 | +0.0537 | [-0.0289, +0.1352] | 0.1914 | 0.7283 | Null: no evidence of an effect at this horizon |
| P08 | pooled | funding_growth_yoy | 2Q | 431 | +0.0642 | [-0.0205, +0.1522] | 0.1888 | 0.7283 | Null: no evidence of an effect at this horizon |
| P09 | pooled | funding_growth_yoy | 4Q | 411 | +0.0098 | [-0.0985, +0.1187] | 0.8364 | 0.9292 | Null: no evidence of an effect at this horizon |
| B-biotech-1q | by_sector | funding_growth_qoq | 1Q | 47 | +0.1829 | n/a | 0.2164 | 0.8113 | Null: no evidence of an effect at this horizon |
| B-biotech-2q | by_sector | funding_growth_qoq | 2Q | 46 | +0.1909 | n/a | 0.2084 | 0.8113 | Null: no evidence of an effect at this horizon |
| B-biotech-4q | by_sector | funding_growth_qoq | 4Q | 44 | +0.1483 | n/a | 0.3341 | 0.8353 | Null: no evidence of an effect at this horizon |
| B-cybersecurity-1q | by_sector | funding_growth_qoq | 1Q | 44 | +0.2347 | n/a | 0.1316 | 0.6579 | Null: no evidence of an effect at this horizon |
| B-cybersecurity-2q | by_sector | funding_growth_qoq | 2Q | 43 | +0.0905 | n/a | 0.5689 | 0.8981 | Null: no evidence of an effect at this horizon |
| B-cybersecurity-4q | by_sector | funding_growth_qoq | 4Q | 41 | +0.0491 | n/a | 0.7592 | 0.9111 | Null: no evidence of an effect at this horizon |
| B-energy-1q | by_sector | funding_growth_qoq | 1Q | 47 | -0.1523 | n/a | 0.2957 | 0.8353 | Null: no evidence of an effect at this horizon |
| B-energy-2q | by_sector | funding_growth_qoq | 2Q | 46 | -0.0770 | n/a | 0.6089 | 0.8981 | Null: no evidence of an effect at this horizon |
| B-energy-4q | by_sector | funding_growth_qoq | 4Q | 44 | +0.1137 | n/a | 0.4625 | 0.8981 | Null: no evidence of an effect at this horizon |
| B-financials-1q | by_sector | funding_growth_qoq | 1Q | 47 | -0.1536 | n/a | 0.3053 | 0.8353 | Null: no evidence of an effect at this horizon |
| B-financials-2q | by_sector | funding_growth_qoq | 2Q | 46 | -0.0189 | n/a | 0.8968 | 0.9584 | Null: no evidence of an effect at this horizon |
| B-financials-4q | by_sector | funding_growth_qoq | 4Q | 44 | +0.0906 | n/a | 0.5633 | 0.8981 | Null: no evidence of an effect at this horizon |
| B-fintech-1q | by_sector | funding_growth_qoq | 1Q | 37 | -0.3810 | n/a | 0.0230 | 0.3449 | Nominally significant but does NOT survive BH correction (or the CI and the permutation test disagree) |
| B-fintech-2q | by_sector | funding_growth_qoq | 2Q | 36 | -0.3199 | n/a | 0.0606 | 0.4544 | Null: no evidence of an effect at this horizon |
| B-fintech-4q | by_sector | funding_growth_qoq | 4Q | 34 | +0.0995 | n/a | 0.5655 | 0.8981 | Null: no evidence of an effect at this horizon |
| B-healthcare-1q | by_sector | funding_growth_qoq | 1Q | 47 | +0.2876 | n/a | 0.0494 | 0.4544 | Nominally significant but does NOT survive BH correction (or the CI and the permutation test disagree) |
| B-healthcare-2q | by_sector | funding_growth_qoq | 2Q | 46 | +0.2598 | n/a | 0.0780 | 0.4679 | Null: no evidence of an effect at this horizon |
| B-healthcare-4q | by_sector | funding_growth_qoq | 4Q | 44 | +0.3550 | n/a | 0.0162 | 0.3449 | Nominally significant but does NOT survive BH correction (or the CI and the permutation test disagree) |
| B-industrials-1q | by_sector | funding_growth_qoq | 1Q | 47 | -0.0119 | n/a | 0.9358 | 0.9584 | Null: no evidence of an effect at this horizon |
| B-industrials-2q | by_sector | funding_growth_qoq | 2Q | 46 | -0.0228 | n/a | 0.8806 | 0.9584 | Null: no evidence of an effect at this horizon |
| B-industrials-4q | by_sector | funding_growth_qoq | 4Q | 44 | -0.0142 | n/a | 0.9294 | 0.9584 | Null: no evidence of an effect at this horizon |
| B-semiconductors-1q | by_sector | funding_growth_qoq | 1Q | 47 | -0.0076 | n/a | 0.9584 | 0.9584 | Null: no evidence of an effect at this horizon |
| B-semiconductors-2q | by_sector | funding_growth_qoq | 2Q | 46 | +0.0585 | n/a | 0.6825 | 0.9111 | Null: no evidence of an effect at this horizon |
| B-semiconductors-4q | by_sector | funding_growth_qoq | 4Q | 44 | +0.0581 | n/a | 0.7035 | 0.9111 | Null: no evidence of an effect at this horizon |
| B-software-1q | by_sector | funding_growth_qoq | 1Q | 47 | -0.0934 | n/a | 0.5283 | 0.8981 | Null: no evidence of an effect at this horizon |
| B-software-2q | by_sector | funding_growth_qoq | 2Q | 46 | +0.0496 | n/a | 0.7397 | 0.9111 | Null: no evidence of an effect at this horizon |
| B-software-4q | by_sector | funding_growth_qoq | 4Q | 44 | -0.1556 | n/a | 0.3183 | 0.8353 | Null: no evidence of an effect at this horizon |
| B-technology-1q | by_sector | funding_growth_qoq | 1Q | 47 | -0.0737 | n/a | 0.6283 | 0.8981 | Null: no evidence of an effect at this horizon |
| B-technology-2q | by_sector | funding_growth_qoq | 2Q | 46 | +0.1282 | n/a | 0.3999 | 0.8981 | Null: no evidence of an effect at this horizon |
| B-technology-4q | by_sector | funding_growth_qoq | 4Q | 44 | -0.0757 | n/a | 0.6287 | 0.8981 | Null: no evidence of an effect at this horizon |
| W01 | walk_forward | funding_growth_qoq | 1Q | 28 | -0.0204 | [-0.0441, +0.0027] | n/a | n/a | Sign agreement in 2/4 folds |
| W02 | walk_forward | funding_growth_qoq | 2Q | 28 | -0.0033 | [-0.0300, +0.0223] | n/a | n/a | Sign agreement in 2/4 folds |
| W03 | walk_forward | funding_growth_qoq | 4Q | 26 | +0.0098 | [-0.0433, +0.0601] | n/a | n/a | Sign agreement in 4/4 folds |

**48 hypothesis tests run; 0 survive Benjamini-Hochberg at q = 0.05 within their family.**

## Entries

### S01 - Cross-sectional tercile sort (top third minus bottom third), funding_growth_qoq, 1Q horizon

- **Protocol:** Each quarter rank sectors by funding_growth_qoq; long the top third, short the bottom third (k = n//3, min 6 sectors); hold 1Q. Statistic: mean quarterly spread (return). 95% CI: paired-by-quarter circular block bootstrap, block = 1 quarters (10,000 resamples, seed 0). Two-sided p: within-quarter permutation of returns (5,000 permutations).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2014Q3..2026Q1, 10 sectors, 457 sector-quarters
- **Result:** estimate -0.0111 (n = 47)
- **95% CI:** [-0.0288, +0.0061]
- **p-value:** 0.2733; BH-adjusted 0.7654
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Mean top-third return -0.0030, bottom-third +0.0082; hit rate (spread > 0) 43% of 47 quarters.

### S02 - Cross-sectional tercile sort (top third minus bottom third), funding_growth_qoq, 2Q horizon

- **Protocol:** Each quarter rank sectors by funding_growth_qoq; long the top third, short the bottom third (k = n//3, min 6 sectors); hold 2Q. Statistic: mean quarterly spread (return). 95% CI: paired-by-quarter circular block bootstrap, block = 2 quarters (10,000 resamples, seed 0). Two-sided p: within-quarter permutation of returns (5,000 permutations).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2014Q3..2025Q4, 10 sectors, 447 sector-quarters
- **Result:** estimate +0.0003 (n = 46)
- **95% CI:** [-0.0221, +0.0229]
- **p-value:** 0.9864; BH-adjusted 0.9864
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Mean top-third return -0.0074, bottom-third -0.0076; hit rate (spread > 0) 52% of 46 quarters.

### S03 - Cross-sectional tercile sort (top third minus bottom third), funding_growth_qoq, 4Q horizon

- **Protocol:** Each quarter rank sectors by funding_growth_qoq; long the top third, short the bottom third (k = n//3, min 6 sectors); hold 4Q. Statistic: mean quarterly spread (return). 95% CI: paired-by-quarter circular block bootstrap, block = 4 quarters (10,000 resamples, seed 0). Two-sided p: within-quarter permutation of returns (5,000 permutations).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2014Q3..2025Q2, 10 sectors, 427 sector-quarters
- **Result:** estimate +0.0152 (n = 44)
- **95% CI:** [-0.0234, +0.0520]
- **p-value:** 0.5103; BH-adjusted 0.7654
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Mean top-third return -0.0094, bottom-third -0.0246; hit rate (spread > 0) 59% of 44 quarters.

### S04 - Cross-sectional tercile sort (top third minus bottom third), deal_growth_qoq, 1Q horizon

- **Protocol:** Each quarter rank sectors by deal_growth_qoq; long the top third, short the bottom third (k = n//3, min 6 sectors); hold 1Q. Statistic: mean quarterly spread (return). 95% CI: paired-by-quarter circular block bootstrap, block = 1 quarters (10,000 resamples, seed 0). Two-sided p: within-quarter permutation of returns (5,000 permutations).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2014Q3..2026Q1, 10 sectors, 457 sector-quarters
- **Result:** estimate -0.0006 (n = 47)
- **95% CI:** [-0.0248, +0.0217]
- **p-value:** 0.9562; BH-adjusted 0.9864
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Mean top-third return -0.0025, bottom-third -0.0019; hit rate (spread > 0) 55% of 47 quarters.

### S05 - Cross-sectional tercile sort (top third minus bottom third), deal_growth_qoq, 2Q horizon

- **Protocol:** Each quarter rank sectors by deal_growth_qoq; long the top third, short the bottom third (k = n//3, min 6 sectors); hold 2Q. Statistic: mean quarterly spread (return). 95% CI: paired-by-quarter circular block bootstrap, block = 2 quarters (10,000 resamples, seed 0). Two-sided p: within-quarter permutation of returns (5,000 permutations).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2014Q3..2025Q4, 10 sectors, 447 sector-quarters
- **Result:** estimate +0.0130 (n = 46)
- **95% CI:** [-0.0119, +0.0365]
- **p-value:** 0.3957; BH-adjusted 0.7654
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Mean top-third return +0.0026, bottom-third -0.0104; hit rate (spread > 0) 63% of 46 quarters.

### S06 - Cross-sectional tercile sort (top third minus bottom third), deal_growth_qoq, 4Q horizon

- **Protocol:** Each quarter rank sectors by deal_growth_qoq; long the top third, short the bottom third (k = n//3, min 6 sectors); hold 4Q. Statistic: mean quarterly spread (return). 95% CI: paired-by-quarter circular block bootstrap, block = 4 quarters (10,000 resamples, seed 0). Two-sided p: within-quarter permutation of returns (5,000 permutations).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2014Q3..2025Q2, 10 sectors, 427 sector-quarters
- **Result:** estimate +0.0320 (n = 44)
- **95% CI:** [+0.0036, +0.0609]
- **p-value:** 0.1576; BH-adjusted 0.7654
- **Verdict:** Nominally significant but does NOT survive BH correction (or the CI and the permutation test disagree). No claim.
- Note: Mean top-third return +0.0034, bottom-third -0.0286; hit rate (spread > 0) 64% of 44 quarters.

### S07 - Cross-sectional tercile sort (top third minus bottom third), funding_growth_yoy, 1Q horizon

- **Protocol:** Each quarter rank sectors by funding_growth_yoy; long the top third, short the bottom third (k = n//3, min 6 sectors); hold 1Q. Statistic: mean quarterly spread (return). 95% CI: paired-by-quarter circular block bootstrap, block = 1 quarters (10,000 resamples, seed 0). Two-sided p: within-quarter permutation of returns (5,000 permutations).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2015Q1..2026Q1, 10 sectors, 441 sector-quarters
- **Result:** estimate +0.0079 (n = 45)
- **95% CI:** [-0.0105, +0.0254]
- **p-value:** 0.4503; BH-adjusted 0.7654
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Mean top-third return +0.0080, bottom-third +0.0001; hit rate (spread > 0) 58% of 45 quarters.

### S08 - Cross-sectional tercile sort (top third minus bottom third), funding_growth_yoy, 2Q horizon

- **Protocol:** Each quarter rank sectors by funding_growth_yoy; long the top third, short the bottom third (k = n//3, min 6 sectors); hold 2Q. Statistic: mean quarterly spread (return). 95% CI: paired-by-quarter circular block bootstrap, block = 2 quarters (10,000 resamples, seed 0). Two-sided p: within-quarter permutation of returns (5,000 permutations).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2015Q1..2025Q4, 10 sectors, 431 sector-quarters
- **Result:** estimate +0.0176 (n = 44)
- **95% CI:** [-0.0139, +0.0503]
- **p-value:** 0.2490; BH-adjusted 0.7654
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Mean top-third return +0.0092, bottom-third -0.0084; hit rate (spread > 0) 52% of 44 quarters.

### S09 - Cross-sectional tercile sort (top third minus bottom third), funding_growth_yoy, 4Q horizon

- **Protocol:** Each quarter rank sectors by funding_growth_yoy; long the top third, short the bottom third (k = n//3, min 6 sectors); hold 4Q. Statistic: mean quarterly spread (return). 95% CI: paired-by-quarter circular block bootstrap, block = 4 quarters (10,000 resamples, seed 0). Two-sided p: within-quarter permutation of returns (5,000 permutations).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2015Q1..2025Q2, 10 sectors, 411 sector-quarters
- **Result:** estimate -0.0009 (n = 42)
- **95% CI:** [-0.0429, +0.0396]
- **p-value:** 0.9632; BH-adjusted 0.9864
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Mean top-third return -0.0025, bottom-third -0.0015; hit rate (spread > 0) 45% of 42 quarters.

### P01 - Pooled Spearman rank correlation, funding_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho between funding_growth_qoq in quarter t and the 1Q forward return from the end of t (+lag), pooled over sector-quarters. 95% CI: percentile cluster bootstrap over quarters (10,000 resamples, seed 0). Two-sided p: permutation of returns within quarter (5,000 permutations).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2014Q3..2026Q1, 10 sectors, 457 sector-quarters
- **Result:** estimate -0.0090 (n = 457)
- **95% CI:** [-0.0997, +0.0783]
- **p-value:** 0.8442; BH-adjusted 0.9292
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: 47 quarter clusters.

### P02 - Pooled Spearman rank correlation, funding_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho between funding_growth_qoq in quarter t and the 2Q forward return from the end of t (+lag), pooled over sector-quarters. 95% CI: percentile cluster bootstrap over quarters (10,000 resamples, seed 0). Two-sided p: permutation of returns within quarter (5,000 permutations).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2014Q3..2025Q4, 10 sectors, 447 sector-quarters
- **Result:** estimate +0.0299 (n = 447)
- **95% CI:** [-0.0525, +0.1110]
- **p-value:** 0.4925; BH-adjusted 0.7388
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: 46 quarter clusters.

### P03 - Pooled Spearman rank correlation, funding_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho between funding_growth_qoq in quarter t and the 4Q forward return from the end of t (+lag), pooled over sector-quarters. 95% CI: percentile cluster bootstrap over quarters (10,000 resamples, seed 0). Two-sided p: permutation of returns within quarter (5,000 permutations).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2014Q3..2025Q2, 10 sectors, 427 sector-quarters
- **Result:** estimate +0.0535 (n = 427)
- **95% CI:** [-0.0410, +0.1457]
- **p-value:** 0.2428; BH-adjusted 0.7283
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: 44 quarter clusters.

### P04 - Pooled Spearman rank correlation, deal_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho between deal_growth_qoq in quarter t and the 1Q forward return from the end of t (+lag), pooled over sector-quarters. 95% CI: percentile cluster bootstrap over quarters (10,000 resamples, seed 0). Two-sided p: permutation of returns within quarter (5,000 permutations).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2014Q3..2026Q1, 10 sectors, 457 sector-quarters
- **Result:** estimate -0.0039 (n = 457)
- **95% CI:** [-0.1021, +0.0907]
- **p-value:** 0.9292; BH-adjusted 0.9292
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: 47 quarter clusters.

### P05 - Pooled Spearman rank correlation, deal_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho between deal_growth_qoq in quarter t and the 2Q forward return from the end of t (+lag), pooled over sector-quarters. 95% CI: percentile cluster bootstrap over quarters (10,000 resamples, seed 0). Two-sided p: permutation of returns within quarter (5,000 permutations).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2014Q3..2025Q4, 10 sectors, 447 sector-quarters
- **Result:** estimate +0.0317 (n = 447)
- **95% CI:** [-0.0533, +0.1226]
- **p-value:** 0.4775; BH-adjusted 0.7388
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: 46 quarter clusters.

### P06 - Pooled Spearman rank correlation, deal_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho between deal_growth_qoq in quarter t and the 4Q forward return from the end of t (+lag), pooled over sector-quarters. 95% CI: percentile cluster bootstrap over quarters (10,000 resamples, seed 0). Two-sided p: permutation of returns within quarter (5,000 permutations).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2014Q3..2025Q2, 10 sectors, 427 sector-quarters
- **Result:** estimate +0.0473 (n = 427)
- **95% CI:** [-0.0498, +0.1439]
- **p-value:** 0.3333; BH-adjusted 0.7388
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: 44 quarter clusters.

### P07 - Pooled Spearman rank correlation, funding_growth_yoy, 1Q horizon

- **Protocol:** Spearman rho between funding_growth_yoy in quarter t and the 1Q forward return from the end of t (+lag), pooled over sector-quarters. 95% CI: percentile cluster bootstrap over quarters (10,000 resamples, seed 0). Two-sided p: permutation of returns within quarter (5,000 permutations).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2015Q1..2026Q1, 10 sectors, 441 sector-quarters
- **Result:** estimate +0.0537 (n = 441)
- **95% CI:** [-0.0289, +0.1352]
- **p-value:** 0.1914; BH-adjusted 0.7283
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: 45 quarter clusters.

### P08 - Pooled Spearman rank correlation, funding_growth_yoy, 2Q horizon

- **Protocol:** Spearman rho between funding_growth_yoy in quarter t and the 2Q forward return from the end of t (+lag), pooled over sector-quarters. 95% CI: percentile cluster bootstrap over quarters (10,000 resamples, seed 0). Two-sided p: permutation of returns within quarter (5,000 permutations).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2015Q1..2025Q4, 10 sectors, 431 sector-quarters
- **Result:** estimate +0.0642 (n = 431)
- **95% CI:** [-0.0205, +0.1522]
- **p-value:** 0.1888; BH-adjusted 0.7283
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: 44 quarter clusters.

### P09 - Pooled Spearman rank correlation, funding_growth_yoy, 4Q horizon

- **Protocol:** Spearman rho between funding_growth_yoy in quarter t and the 4Q forward return from the end of t (+lag), pooled over sector-quarters. 95% CI: percentile cluster bootstrap over quarters (10,000 resamples, seed 0). Two-sided p: permutation of returns within quarter (5,000 permutations).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2015Q1..2025Q2, 10 sectors, 411 sector-quarters
- **Result:** estimate +0.0098 (n = 411)
- **95% CI:** [-0.0985, +0.1187]
- **p-value:** 0.8364; BH-adjusted 0.9292
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: 42 quarter clusters.

### B-biotech-1q - Per-sector Spearman (biotech), funding_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 1Q forward return within sector 'biotech'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2014Q3..2026Q1, 1 sectors, 47 sector-quarters
- **Result:** estimate +0.1829 (n = 47)
- **95% CI:** n/a
- **p-value:** 0.2164; BH-adjusted 0.8113
- **Verdict:** Null: no evidence of an effect at this horizon.

### B-biotech-2q - Per-sector Spearman (biotech), funding_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 2Q forward return within sector 'biotech'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2014Q3..2025Q4, 1 sectors, 46 sector-quarters
- **Result:** estimate +0.1909 (n = 46)
- **95% CI:** n/a
- **p-value:** 0.2084; BH-adjusted 0.8113
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-biotech-4q - Per-sector Spearman (biotech), funding_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 4Q forward return within sector 'biotech'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2014Q3..2025Q2, 1 sectors, 44 sector-quarters
- **Result:** estimate +0.1483 (n = 44)
- **95% CI:** n/a
- **p-value:** 0.3341; BH-adjusted 0.8353
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-cybersecurity-1q - Per-sector Spearman (cybersecurity), funding_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 1Q forward return within sector 'cybersecurity'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2015Q2..2026Q1, 1 sectors, 44 sector-quarters
- **Result:** estimate +0.2347 (n = 44)
- **95% CI:** n/a
- **p-value:** 0.1316; BH-adjusted 0.6579
- **Verdict:** Null: no evidence of an effect at this horizon.

### B-cybersecurity-2q - Per-sector Spearman (cybersecurity), funding_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 2Q forward return within sector 'cybersecurity'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2015Q2..2025Q4, 1 sectors, 43 sector-quarters
- **Result:** estimate +0.0905 (n = 43)
- **95% CI:** n/a
- **p-value:** 0.5689; BH-adjusted 0.8981
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-cybersecurity-4q - Per-sector Spearman (cybersecurity), funding_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 4Q forward return within sector 'cybersecurity'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2015Q2..2025Q2, 1 sectors, 41 sector-quarters
- **Result:** estimate +0.0491 (n = 41)
- **95% CI:** n/a
- **p-value:** 0.7592; BH-adjusted 0.9111
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-energy-1q - Per-sector Spearman (energy), funding_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 1Q forward return within sector 'energy'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2014Q3..2026Q1, 1 sectors, 47 sector-quarters
- **Result:** estimate -0.1523 (n = 47)
- **95% CI:** n/a
- **p-value:** 0.2957; BH-adjusted 0.8353
- **Verdict:** Null: no evidence of an effect at this horizon.

### B-energy-2q - Per-sector Spearman (energy), funding_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 2Q forward return within sector 'energy'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2014Q3..2025Q4, 1 sectors, 46 sector-quarters
- **Result:** estimate -0.0770 (n = 46)
- **95% CI:** n/a
- **p-value:** 0.6089; BH-adjusted 0.8981
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-energy-4q - Per-sector Spearman (energy), funding_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 4Q forward return within sector 'energy'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2014Q3..2025Q2, 1 sectors, 44 sector-quarters
- **Result:** estimate +0.1137 (n = 44)
- **95% CI:** n/a
- **p-value:** 0.4625; BH-adjusted 0.8981
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-financials-1q - Per-sector Spearman (financials), funding_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 1Q forward return within sector 'financials'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2014Q3..2026Q1, 1 sectors, 47 sector-quarters
- **Result:** estimate -0.1536 (n = 47)
- **95% CI:** n/a
- **p-value:** 0.3053; BH-adjusted 0.8353
- **Verdict:** Null: no evidence of an effect at this horizon.

### B-financials-2q - Per-sector Spearman (financials), funding_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 2Q forward return within sector 'financials'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2014Q3..2025Q4, 1 sectors, 46 sector-quarters
- **Result:** estimate -0.0189 (n = 46)
- **95% CI:** n/a
- **p-value:** 0.8968; BH-adjusted 0.9584
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-financials-4q - Per-sector Spearman (financials), funding_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 4Q forward return within sector 'financials'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2014Q3..2025Q2, 1 sectors, 44 sector-quarters
- **Result:** estimate +0.0906 (n = 44)
- **95% CI:** n/a
- **p-value:** 0.5633; BH-adjusted 0.8981
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-fintech-1q - Per-sector Spearman (fintech), funding_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 1Q forward return within sector 'fintech'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2017Q1..2026Q1, 1 sectors, 37 sector-quarters
- **Result:** estimate -0.3810 (n = 37)
- **95% CI:** n/a
- **p-value:** 0.0230; BH-adjusted 0.3449
- **Verdict:** Nominally significant but does NOT survive BH correction (or the CI and the permutation test disagree). No claim.

### B-fintech-2q - Per-sector Spearman (fintech), funding_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 2Q forward return within sector 'fintech'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2017Q1..2025Q4, 1 sectors, 36 sector-quarters
- **Result:** estimate -0.3199 (n = 36)
- **95% CI:** n/a
- **p-value:** 0.0606; BH-adjusted 0.4544
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-fintech-4q - Per-sector Spearman (fintech), funding_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 4Q forward return within sector 'fintech'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2017Q1..2025Q2, 1 sectors, 34 sector-quarters
- **Result:** estimate +0.0995 (n = 34)
- **95% CI:** n/a
- **p-value:** 0.5655; BH-adjusted 0.8981
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-healthcare-1q - Per-sector Spearman (healthcare), funding_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 1Q forward return within sector 'healthcare'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2014Q3..2026Q1, 1 sectors, 47 sector-quarters
- **Result:** estimate +0.2876 (n = 47)
- **95% CI:** n/a
- **p-value:** 0.0494; BH-adjusted 0.4544
- **Verdict:** Nominally significant but does NOT survive BH correction (or the CI and the permutation test disagree). No claim.

### B-healthcare-2q - Per-sector Spearman (healthcare), funding_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 2Q forward return within sector 'healthcare'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2014Q3..2025Q4, 1 sectors, 46 sector-quarters
- **Result:** estimate +0.2598 (n = 46)
- **95% CI:** n/a
- **p-value:** 0.0780; BH-adjusted 0.4679
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-healthcare-4q - Per-sector Spearman (healthcare), funding_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 4Q forward return within sector 'healthcare'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2014Q3..2025Q2, 1 sectors, 44 sector-quarters
- **Result:** estimate +0.3550 (n = 44)
- **95% CI:** n/a
- **p-value:** 0.0162; BH-adjusted 0.3449
- **Verdict:** Nominally significant but does NOT survive BH correction (or the CI and the permutation test disagree). No claim.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-industrials-1q - Per-sector Spearman (industrials), funding_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 1Q forward return within sector 'industrials'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2014Q3..2026Q1, 1 sectors, 47 sector-quarters
- **Result:** estimate -0.0119 (n = 47)
- **95% CI:** n/a
- **p-value:** 0.9358; BH-adjusted 0.9584
- **Verdict:** Null: no evidence of an effect at this horizon.

### B-industrials-2q - Per-sector Spearman (industrials), funding_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 2Q forward return within sector 'industrials'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2014Q3..2025Q4, 1 sectors, 46 sector-quarters
- **Result:** estimate -0.0228 (n = 46)
- **95% CI:** n/a
- **p-value:** 0.8806; BH-adjusted 0.9584
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-industrials-4q - Per-sector Spearman (industrials), funding_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 4Q forward return within sector 'industrials'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2014Q3..2025Q2, 1 sectors, 44 sector-quarters
- **Result:** estimate -0.0142 (n = 44)
- **95% CI:** n/a
- **p-value:** 0.9294; BH-adjusted 0.9584
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-semiconductors-1q - Per-sector Spearman (semiconductors), funding_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 1Q forward return within sector 'semiconductors'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2014Q3..2026Q1, 1 sectors, 47 sector-quarters
- **Result:** estimate -0.0076 (n = 47)
- **95% CI:** n/a
- **p-value:** 0.9584; BH-adjusted 0.9584
- **Verdict:** Null: no evidence of an effect at this horizon.

### B-semiconductors-2q - Per-sector Spearman (semiconductors), funding_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 2Q forward return within sector 'semiconductors'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2014Q3..2025Q4, 1 sectors, 46 sector-quarters
- **Result:** estimate +0.0585 (n = 46)
- **95% CI:** n/a
- **p-value:** 0.6825; BH-adjusted 0.9111
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-semiconductors-4q - Per-sector Spearman (semiconductors), funding_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 4Q forward return within sector 'semiconductors'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2014Q3..2025Q2, 1 sectors, 44 sector-quarters
- **Result:** estimate +0.0581 (n = 44)
- **95% CI:** n/a
- **p-value:** 0.7035; BH-adjusted 0.9111
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-software-1q - Per-sector Spearman (software), funding_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 1Q forward return within sector 'software'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2014Q3..2026Q1, 1 sectors, 47 sector-quarters
- **Result:** estimate -0.0934 (n = 47)
- **95% CI:** n/a
- **p-value:** 0.5283; BH-adjusted 0.8981
- **Verdict:** Null: no evidence of an effect at this horizon.

### B-software-2q - Per-sector Spearman (software), funding_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 2Q forward return within sector 'software'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2014Q3..2025Q4, 1 sectors, 46 sector-quarters
- **Result:** estimate +0.0496 (n = 46)
- **95% CI:** n/a
- **p-value:** 0.7397; BH-adjusted 0.9111
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-software-4q - Per-sector Spearman (software), funding_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 4Q forward return within sector 'software'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2014Q3..2025Q2, 1 sectors, 44 sector-quarters
- **Result:** estimate -0.1556 (n = 44)
- **95% CI:** n/a
- **p-value:** 0.3183; BH-adjusted 0.8353
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-technology-1q - Per-sector Spearman (technology), funding_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 1Q forward return within sector 'technology'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2014Q3..2026Q1, 1 sectors, 47 sector-quarters
- **Result:** estimate -0.0737 (n = 47)
- **95% CI:** n/a
- **p-value:** 0.6283; BH-adjusted 0.8981
- **Verdict:** Null: no evidence of an effect at this horizon.

### B-technology-2q - Per-sector Spearman (technology), funding_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 2Q forward return within sector 'technology'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2014Q3..2025Q4, 1 sectors, 46 sector-quarters
- **Result:** estimate +0.1282 (n = 46)
- **95% CI:** n/a
- **p-value:** 0.3999; BH-adjusted 0.8981
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-technology-4q - Per-sector Spearman (technology), funding_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 4Q forward return within sector 'technology'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2014Q3..2025Q2, 1 sectors, 44 sector-quarters
- **Result:** estimate -0.0757 (n = 44)
- **95% CI:** n/a
- **p-value:** 0.6287; BH-adjusted 0.8981
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### W01 - Walk-forward sign persistence of the tercile spread, funding_growth_qoq, 1Q horizon

- **Protocol:** Expanding-window walk-forward with 4 test folds over the quarterly spread series from S01; first 40% of quarters is the initial training window. Report per-fold train/test mean spread and sign agreement, plus the pooled OOS mean with a block bootstrap CI (block = 1, 10,000 resamples, seed 0).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2014Q3..2026Q1, 10 sectors, 457 sector-quarters
- **Result:** estimate -0.0204 (n = 28)
- **95% CI:** [-0.0441, +0.0027]
- **p-value:** n/a
- **Verdict:** Sign agreement in 2/4 folds. OOS CI includes 0. Descriptive: no hypothesis test entered into BH.
- Note: Fold 1: train to 2019Q1 mean +0.0027; test 2019Q2..2020Q4 (n=7) mean -0.0137; DISAGREE
- Note: Fold 2: train to 2020Q4 mean -0.0017; test 2021Q1..2022Q3 (n=7) mean -0.0265; agree
- Note: Fold 3: train to 2022Q3 mean -0.0070; test 2022Q4..2024Q2 (n=7) mean +0.0010; DISAGREE
- Note: Fold 4: train to 2024Q2 mean -0.0056; test 2024Q3..2026Q1 (n=7) mean -0.0426; agree

### W02 - Walk-forward sign persistence of the tercile spread, funding_growth_qoq, 2Q horizon

- **Protocol:** Expanding-window walk-forward with 4 test folds over the quarterly spread series from S02; first 40% of quarters is the initial training window. Report per-fold train/test mean spread and sign agreement, plus the pooled OOS mean with a block bootstrap CI (block = 2, 10,000 resamples, seed 0).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2014Q3..2025Q4, 10 sectors, 447 sector-quarters
- **Result:** estimate -0.0033 (n = 28)
- **95% CI:** [-0.0300, +0.0223]
- **p-value:** n/a
- **Verdict:** Sign agreement in 2/4 folds. OOS CI includes 0. Descriptive: no hypothesis test entered into BH.
- Note: Fold 1: train to 2018Q4 mean +0.0058; test 2019Q1..2020Q3 (n=7) mean +0.0009; agree
- Note: Fold 2: train to 2020Q3 mean +0.0044; test 2020Q4..2022Q2 (n=7) mean -0.0222; DISAGREE
- Note: Fold 3: train to 2022Q2 mean -0.0014; test 2022Q3..2024Q1 (n=7) mean -0.0176; agree
- Note: Fold 4: train to 2024Q1 mean -0.0043; test 2024Q2..2025Q4 (n=7) mean +0.0257; DISAGREE

### W03 - Walk-forward sign persistence of the tercile spread, funding_growth_qoq, 4Q horizon

- **Protocol:** Expanding-window walk-forward with 4 test folds over the quarterly spread series from S03; first 40% of quarters is the initial training window. Report per-fold train/test mean spread and sign agreement, plus the pooled OOS mean with a block bootstrap CI (block = 4, 10,000 resamples, seed 0).
- **Data:** SYNTHETIC fixture (FAKE data); returns=excess, lag=0q; 2014Q3..2025Q2, 10 sectors, 427 sector-quarters
- **Result:** estimate +0.0098 (n = 26)
- **95% CI:** [-0.0433, +0.0601]
- **p-value:** n/a
- **Verdict:** Sign agreement in 4/4 folds. OOS CI includes 0. Descriptive: no hypothesis test entered into BH.
- Note: Fold 1: train to 2018Q4 mean +0.0231; test 2019Q1..2020Q2 (n=6) mean +0.0029; agree
- Note: Fold 2: train to 2020Q2 mean +0.0181; test 2020Q3..2022Q1 (n=7) mean +0.0046; agree
- Note: Fold 3: train to 2022Q1 mean +0.0150; test 2022Q2..2023Q4 (n=7) mean +0.0020; agree
- Note: Fold 4: train to 2023Q4 mean +0.0126; test 2024Q1..2025Q2 (n=6) mean +0.0317; agree
