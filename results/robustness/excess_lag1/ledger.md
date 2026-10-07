# Experiment ledger

Generated 2026-10-06 at commit `1d204db` by `scripts/run_experiments.py`.

## Run configuration

| setting | value |
|---|---|
| synthetic | False |
| private_source | pitchbook_export.csv |
| return_mode | excess |
| signal_lag_quarters | 1 |
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
| S01 | sorts | funding_growth_qoq | 1Q | 47 | +0.0133 | [-0.0067, +0.0339] | 0.1898 | 0.3416 | Null: no evidence of an effect at this horizon |
| S02 | sorts | funding_growth_qoq | 2Q | 46 | +0.0133 | [-0.0139, +0.0394] | 0.3861 | 0.5792 | Null: no evidence of an effect at this horizon |
| S03 | sorts | funding_growth_qoq | 4Q | 44 | -0.0063 | [-0.0342, +0.0216] | 0.7810 | 0.7810 | Null: no evidence of an effect at this horizon |
| S04 | sorts | deal_growth_qoq | 1Q | 47 | +0.0169 | [-0.0028, +0.0358] | 0.1012 | 0.2708 | Null: no evidence of an effect at this horizon |
| S05 | sorts | deal_growth_qoq | 2Q | 46 | +0.0113 | [-0.0150, +0.0366] | 0.4619 | 0.5939 | Null: no evidence of an effect at this horizon |
| S06 | sorts | deal_growth_qoq | 4Q | 44 | -0.0126 | [-0.0553, +0.0236] | 0.5855 | 0.6587 | Null: no evidence of an effect at this horizon |
| S07 | sorts | funding_growth_yoy | 1Q | 44 | -0.0247 | [-0.0441, -0.0056] | 0.0232 | 0.1044 | Nominally significant but does NOT survive BH correction (or the CI and the permutation test disagree) |
| S08 | sorts | funding_growth_yoy | 2Q | 43 | -0.0241 | [-0.0516, +0.0046] | 0.1204 | 0.2708 | Null: no evidence of an effect at this horizon |
| S09 | sorts | funding_growth_yoy | 4Q | 41 | -0.0554 | [-0.1117, -0.0052] | 0.0194 | 0.1044 | Nominally significant but does NOT survive BH correction (or the CI and the permutation test disagree) |
| P01 | pooled | funding_growth_qoq | 1Q | 457 | +0.0641 | [-0.0438, +0.1752] | 0.1446 | 0.4337 | Null: no evidence of an effect at this horizon |
| P02 | pooled | funding_growth_qoq | 2Q | 447 | +0.0413 | [-0.0528, +0.1326] | 0.3291 | 0.7406 | Null: no evidence of an effect at this horizon |
| P03 | pooled | funding_growth_qoq | 4Q | 427 | -0.0284 | [-0.1369, +0.0785] | 0.5165 | 0.7747 | Null: no evidence of an effect at this horizon |
| P04 | pooled | deal_growth_qoq | 1Q | 457 | +0.0099 | [-0.1129, +0.1289] | 0.8654 | 0.8654 | Null: no evidence of an effect at this horizon |
| P05 | pooled | deal_growth_qoq | 2Q | 447 | -0.0259 | [-0.1330, +0.0848] | 0.7377 | 0.8299 | Null: no evidence of an effect at this horizon |
| P06 | pooled | deal_growth_qoq | 4Q | 427 | +0.0142 | [-0.0812, +0.1019] | 0.6981 | 0.8299 | Null: no evidence of an effect at this horizon |
| P07 | pooled | funding_growth_yoy | 1Q | 433 | -0.0449 | [-0.1468, +0.0551] | 0.4197 | 0.7555 | Null: no evidence of an effect at this horizon |
| P08 | pooled | funding_growth_yoy | 2Q | 423 | -0.0785 | [-0.1795, +0.0234] | 0.1240 | 0.4337 | Null: no evidence of an effect at this horizon |
| P09 | pooled | funding_growth_yoy | 4Q | 403 | -0.1116 | [-0.2094, -0.0149] | 0.0336 | 0.3023 | Nominally significant but does NOT survive BH correction (or the CI and the permutation test disagree) |
| B-biotech-1q | by_sector | funding_growth_qoq | 1Q | 47 | +0.3934 | n/a | 0.0062 | 0.1860 | Nominally significant but does NOT survive BH correction (or the CI and the permutation test disagree) |
| B-biotech-2q | by_sector | funding_growth_qoq | 2Q | 46 | +0.2921 | n/a | 0.0476 | 0.7139 | Nominally significant but does NOT survive BH correction (or the CI and the permutation test disagree) |
| B-biotech-4q | by_sector | funding_growth_qoq | 4Q | 44 | +0.0837 | n/a | 0.5945 | 0.9238 | Null: no evidence of an effect at this horizon |
| B-cybersecurity-1q | by_sector | funding_growth_qoq | 1Q | 44 | -0.1790 | n/a | 0.2446 | 0.9238 | Null: no evidence of an effect at this horizon |
| B-cybersecurity-2q | by_sector | funding_growth_qoq | 2Q | 43 | -0.0580 | n/a | 0.7025 | 0.9238 | Null: no evidence of an effect at this horizon |
| B-cybersecurity-4q | by_sector | funding_growth_qoq | 4Q | 41 | -0.0598 | n/a | 0.7083 | 0.9238 | Null: no evidence of an effect at this horizon |
| B-energy-1q | by_sector | funding_growth_qoq | 1Q | 47 | +0.0633 | n/a | 0.6765 | 0.9238 | Null: no evidence of an effect at this horizon |
| B-energy-2q | by_sector | funding_growth_qoq | 2Q | 46 | +0.0665 | n/a | 0.6547 | 0.9238 | Null: no evidence of an effect at this horizon |
| B-energy-4q | by_sector | funding_growth_qoq | 4Q | 44 | +0.0265 | n/a | 0.8706 | 0.9785 | Null: no evidence of an effect at this horizon |
| B-financials-1q | by_sector | funding_growth_qoq | 1Q | 47 | +0.2381 | n/a | 0.1114 | 0.9088 | Null: no evidence of an effect at this horizon |
| B-financials-2q | by_sector | funding_growth_qoq | 2Q | 46 | +0.1248 | n/a | 0.4087 | 0.9238 | Null: no evidence of an effect at this horizon |
| B-financials-4q | by_sector | funding_growth_qoq | 4Q | 44 | +0.0782 | n/a | 0.6137 | 0.9238 | Null: no evidence of an effect at this horizon |
| B-fintech-1q | by_sector | funding_growth_qoq | 1Q | 37 | -0.1970 | n/a | 0.2460 | 0.9238 | Null: no evidence of an effect at this horizon |
| B-fintech-2q | by_sector | funding_growth_qoq | 2Q | 36 | -0.1027 | n/a | 0.5485 | 0.9238 | Null: no evidence of an effect at this horizon |
| B-fintech-4q | by_sector | funding_growth_qoq | 4Q | 34 | -0.1731 | n/a | 0.3409 | 0.9238 | Null: no evidence of an effect at this horizon |
| B-healthcare-1q | by_sector | funding_growth_qoq | 1Q | 47 | -0.1512 | n/a | 0.3107 | 0.9238 | Null: no evidence of an effect at this horizon |
| B-healthcare-2q | by_sector | funding_growth_qoq | 2Q | 46 | -0.0012 | n/a | 0.9940 | 0.9956 | Null: no evidence of an effect at this horizon |
| B-healthcare-4q | by_sector | funding_growth_qoq | 4Q | 44 | -0.0365 | n/a | 0.8120 | 0.9785 | Null: no evidence of an effect at this horizon |
| B-industrials-1q | by_sector | funding_growth_qoq | 1Q | 47 | +0.1189 | n/a | 0.4245 | 0.9238 | Null: no evidence of an effect at this horizon |
| B-industrials-2q | by_sector | funding_growth_qoq | 2Q | 46 | -0.0974 | n/a | 0.5163 | 0.9238 | Null: no evidence of an effect at this horizon |
| B-industrials-4q | by_sector | funding_growth_qoq | 4Q | 44 | -0.1369 | n/a | 0.3719 | 0.9238 | Null: no evidence of an effect at this horizon |
| B-semiconductors-1q | by_sector | funding_growth_qoq | 1Q | 47 | +0.0296 | n/a | 0.8470 | 0.9785 | Null: no evidence of an effect at this horizon |
| B-semiconductors-2q | by_sector | funding_growth_qoq | 2Q | 46 | -0.0096 | n/a | 0.9552 | 0.9956 | Null: no evidence of an effect at this horizon |
| B-semiconductors-4q | by_sector | funding_growth_qoq | 4Q | 44 | +0.0007 | n/a | 0.9956 | 0.9956 | Null: no evidence of an effect at this horizon |
| B-software-1q | by_sector | funding_growth_qoq | 1Q | 47 | +0.0237 | n/a | 0.8806 | 0.9785 | Null: no evidence of an effect at this horizon |
| B-software-2q | by_sector | funding_growth_qoq | 2Q | 46 | -0.0901 | n/a | 0.5389 | 0.9238 | Null: no evidence of an effect at this horizon |
| B-software-4q | by_sector | funding_growth_qoq | 4Q | 44 | -0.2392 | n/a | 0.1212 | 0.9088 | Null: no evidence of an effect at this horizon |
| B-technology-1q | by_sector | funding_growth_qoq | 1Q | 47 | -0.0861 | n/a | 0.5635 | 0.9238 | Null: no evidence of an effect at this horizon |
| B-technology-2q | by_sector | funding_growth_qoq | 2Q | 46 | -0.1007 | n/a | 0.4925 | 0.9238 | Null: no evidence of an effect at this horizon |
| B-technology-4q | by_sector | funding_growth_qoq | 4Q | 44 | -0.1122 | n/a | 0.4591 | 0.9238 | Null: no evidence of an effect at this horizon |
| W01 | walk_forward | funding_growth_qoq | 1Q | 28 | +0.0139 | [-0.0161, +0.0452] | n/a | n/a | Sign agreement in 3/4 folds |
| W02 | walk_forward | funding_growth_qoq | 2Q | 28 | +0.0076 | [-0.0293, +0.0432] | n/a | n/a | Sign agreement in 2/4 folds |
| W03 | walk_forward | funding_growth_qoq | 4Q | 26 | -0.0084 | [-0.0499, +0.0322] | n/a | n/a | Sign agreement in 3/4 folds |

**48 hypothesis tests run; 0 survive Benjamini-Hochberg at q = 0.05 within their family.**

## Entries

### S01 - Cross-sectional tercile sort (top third minus bottom third), funding_growth_qoq, 1Q horizon

- **Protocol:** Each quarter rank sectors by funding_growth_qoq; long the top third, short the bottom third (k = n//3, min 6 sectors); hold 1Q. Statistic: mean quarterly spread (return). 95% CI: paired-by-quarter circular block bootstrap, block = 1 quarters (10,000 resamples, seed 0). Two-sided p: within-quarter permutation of returns (5,000 permutations).
- **Data:** PitchBook export; returns=excess, lag=1q; 2014Q2..2025Q4, 10 sectors, 457 sector-quarters
- **Result:** estimate +0.0133 (n = 47)
- **95% CI:** [-0.0067, +0.0339]
- **p-value:** 0.1898; BH-adjusted 0.3416
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Mean top-third return +0.0066, bottom-third -0.0067; hit rate (spread > 0) 57% of 47 quarters.

### S02 - Cross-sectional tercile sort (top third minus bottom third), funding_growth_qoq, 2Q horizon

- **Protocol:** Each quarter rank sectors by funding_growth_qoq; long the top third, short the bottom third (k = n//3, min 6 sectors); hold 2Q. Statistic: mean quarterly spread (return). 95% CI: paired-by-quarter circular block bootstrap, block = 2 quarters (10,000 resamples, seed 0). Two-sided p: within-quarter permutation of returns (5,000 permutations).
- **Data:** PitchBook export; returns=excess, lag=1q; 2014Q2..2025Q3, 10 sectors, 447 sector-quarters
- **Result:** estimate +0.0133 (n = 46)
- **95% CI:** [-0.0139, +0.0394]
- **p-value:** 0.3861; BH-adjusted 0.5792
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Mean top-third return +0.0068, bottom-third -0.0065; hit rate (spread > 0) 57% of 46 quarters.

### S03 - Cross-sectional tercile sort (top third minus bottom third), funding_growth_qoq, 4Q horizon

- **Protocol:** Each quarter rank sectors by funding_growth_qoq; long the top third, short the bottom third (k = n//3, min 6 sectors); hold 4Q. Statistic: mean quarterly spread (return). 95% CI: paired-by-quarter circular block bootstrap, block = 4 quarters (10,000 resamples, seed 0). Two-sided p: within-quarter permutation of returns (5,000 permutations).
- **Data:** PitchBook export; returns=excess, lag=1q; 2014Q2..2025Q1, 10 sectors, 427 sector-quarters
- **Result:** estimate -0.0063 (n = 44)
- **95% CI:** [-0.0342, +0.0216]
- **p-value:** 0.7810; BH-adjusted 0.7810
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Mean top-third return -0.0102, bottom-third -0.0038; hit rate (spread > 0) 52% of 44 quarters.

### S04 - Cross-sectional tercile sort (top third minus bottom third), deal_growth_qoq, 1Q horizon

- **Protocol:** Each quarter rank sectors by deal_growth_qoq; long the top third, short the bottom third (k = n//3, min 6 sectors); hold 1Q. Statistic: mean quarterly spread (return). 95% CI: paired-by-quarter circular block bootstrap, block = 1 quarters (10,000 resamples, seed 0). Two-sided p: within-quarter permutation of returns (5,000 permutations).
- **Data:** PitchBook export; returns=excess, lag=1q; 2014Q2..2025Q4, 10 sectors, 457 sector-quarters
- **Result:** estimate +0.0169 (n = 47)
- **95% CI:** [-0.0028, +0.0358]
- **p-value:** 0.1012; BH-adjusted 0.2708
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Mean top-third return +0.0058, bottom-third -0.0111; hit rate (spread > 0) 62% of 47 quarters.

### S05 - Cross-sectional tercile sort (top third minus bottom third), deal_growth_qoq, 2Q horizon

- **Protocol:** Each quarter rank sectors by deal_growth_qoq; long the top third, short the bottom third (k = n//3, min 6 sectors); hold 2Q. Statistic: mean quarterly spread (return). 95% CI: paired-by-quarter circular block bootstrap, block = 2 quarters (10,000 resamples, seed 0). Two-sided p: within-quarter permutation of returns (5,000 permutations).
- **Data:** PitchBook export; returns=excess, lag=1q; 2014Q2..2025Q3, 10 sectors, 447 sector-quarters
- **Result:** estimate +0.0113 (n = 46)
- **95% CI:** [-0.0150, +0.0366]
- **p-value:** 0.4619; BH-adjusted 0.5939
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Mean top-third return +0.0012, bottom-third -0.0101; hit rate (spread > 0) 54% of 46 quarters.

### S06 - Cross-sectional tercile sort (top third minus bottom third), deal_growth_qoq, 4Q horizon

- **Protocol:** Each quarter rank sectors by deal_growth_qoq; long the top third, short the bottom third (k = n//3, min 6 sectors); hold 4Q. Statistic: mean quarterly spread (return). 95% CI: paired-by-quarter circular block bootstrap, block = 4 quarters (10,000 resamples, seed 0). Two-sided p: within-quarter permutation of returns (5,000 permutations).
- **Data:** PitchBook export; returns=excess, lag=1q; 2014Q2..2025Q1, 10 sectors, 427 sector-quarters
- **Result:** estimate -0.0126 (n = 44)
- **95% CI:** [-0.0553, +0.0236]
- **p-value:** 0.5855; BH-adjusted 0.6587
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Mean top-third return -0.0128, bottom-third -0.0001; hit rate (spread > 0) 45% of 44 quarters.

### S07 - Cross-sectional tercile sort (top third minus bottom third), funding_growth_yoy, 1Q horizon

- **Protocol:** Each quarter rank sectors by funding_growth_yoy; long the top third, short the bottom third (k = n//3, min 6 sectors); hold 1Q. Statistic: mean quarterly spread (return). 95% CI: paired-by-quarter circular block bootstrap, block = 1 quarters (10,000 resamples, seed 0). Two-sided p: within-quarter permutation of returns (5,000 permutations).
- **Data:** PitchBook export; returns=excess, lag=1q; 2015Q1..2025Q4, 10 sectors, 433 sector-quarters
- **Result:** estimate -0.0247 (n = 44)
- **95% CI:** [-0.0441, -0.0056]
- **p-value:** 0.0232; BH-adjusted 0.1044
- **Verdict:** Nominally significant but does NOT survive BH correction (or the CI and the permutation test disagree). No claim.
- Note: Mean top-third return -0.0116, bottom-third +0.0130; hit rate (spread > 0) 41% of 44 quarters.

### S08 - Cross-sectional tercile sort (top third minus bottom third), funding_growth_yoy, 2Q horizon

- **Protocol:** Each quarter rank sectors by funding_growth_yoy; long the top third, short the bottom third (k = n//3, min 6 sectors); hold 2Q. Statistic: mean quarterly spread (return). 95% CI: paired-by-quarter circular block bootstrap, block = 2 quarters (10,000 resamples, seed 0). Two-sided p: within-quarter permutation of returns (5,000 permutations).
- **Data:** PitchBook export; returns=excess, lag=1q; 2015Q1..2025Q3, 10 sectors, 423 sector-quarters
- **Result:** estimate -0.0241 (n = 43)
- **95% CI:** [-0.0516, +0.0046]
- **p-value:** 0.1204; BH-adjusted 0.2708
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Mean top-third return -0.0137, bottom-third +0.0104; hit rate (spread > 0) 37% of 43 quarters.

### S09 - Cross-sectional tercile sort (top third minus bottom third), funding_growth_yoy, 4Q horizon

- **Protocol:** Each quarter rank sectors by funding_growth_yoy; long the top third, short the bottom third (k = n//3, min 6 sectors); hold 4Q. Statistic: mean quarterly spread (return). 95% CI: paired-by-quarter circular block bootstrap, block = 4 quarters (10,000 resamples, seed 0). Two-sided p: within-quarter permutation of returns (5,000 permutations).
- **Data:** PitchBook export; returns=excess, lag=1q; 2015Q1..2025Q1, 10 sectors, 403 sector-quarters
- **Result:** estimate -0.0554 (n = 41)
- **95% CI:** [-0.1117, -0.0052]
- **p-value:** 0.0194; BH-adjusted 0.1044
- **Verdict:** Nominally significant but does NOT survive BH correction (or the CI and the permutation test disagree). No claim.
- Note: Mean top-third return -0.0418, bottom-third +0.0136; hit rate (spread > 0) 44% of 41 quarters.

### P01 - Pooled Spearman rank correlation, funding_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho between funding_growth_qoq in quarter t and the 1Q forward return from the end of t (+lag), pooled over sector-quarters. 95% CI: percentile cluster bootstrap over quarters (10,000 resamples, seed 0). Two-sided p: permutation of returns within quarter (5,000 permutations).
- **Data:** PitchBook export; returns=excess, lag=1q; 2014Q2..2025Q4, 10 sectors, 457 sector-quarters
- **Result:** estimate +0.0641 (n = 457)
- **95% CI:** [-0.0438, +0.1752]
- **p-value:** 0.1446; BH-adjusted 0.4337
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: 47 quarter clusters.

### P02 - Pooled Spearman rank correlation, funding_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho between funding_growth_qoq in quarter t and the 2Q forward return from the end of t (+lag), pooled over sector-quarters. 95% CI: percentile cluster bootstrap over quarters (10,000 resamples, seed 0). Two-sided p: permutation of returns within quarter (5,000 permutations).
- **Data:** PitchBook export; returns=excess, lag=1q; 2014Q2..2025Q3, 10 sectors, 447 sector-quarters
- **Result:** estimate +0.0413 (n = 447)
- **95% CI:** [-0.0528, +0.1326]
- **p-value:** 0.3291; BH-adjusted 0.7406
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: 46 quarter clusters.

### P03 - Pooled Spearman rank correlation, funding_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho between funding_growth_qoq in quarter t and the 4Q forward return from the end of t (+lag), pooled over sector-quarters. 95% CI: percentile cluster bootstrap over quarters (10,000 resamples, seed 0). Two-sided p: permutation of returns within quarter (5,000 permutations).
- **Data:** PitchBook export; returns=excess, lag=1q; 2014Q2..2025Q1, 10 sectors, 427 sector-quarters
- **Result:** estimate -0.0284 (n = 427)
- **95% CI:** [-0.1369, +0.0785]
- **p-value:** 0.5165; BH-adjusted 0.7747
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: 44 quarter clusters.

### P04 - Pooled Spearman rank correlation, deal_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho between deal_growth_qoq in quarter t and the 1Q forward return from the end of t (+lag), pooled over sector-quarters. 95% CI: percentile cluster bootstrap over quarters (10,000 resamples, seed 0). Two-sided p: permutation of returns within quarter (5,000 permutations).
- **Data:** PitchBook export; returns=excess, lag=1q; 2014Q2..2025Q4, 10 sectors, 457 sector-quarters
- **Result:** estimate +0.0099 (n = 457)
- **95% CI:** [-0.1129, +0.1289]
- **p-value:** 0.8654; BH-adjusted 0.8654
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: 47 quarter clusters.

### P05 - Pooled Spearman rank correlation, deal_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho between deal_growth_qoq in quarter t and the 2Q forward return from the end of t (+lag), pooled over sector-quarters. 95% CI: percentile cluster bootstrap over quarters (10,000 resamples, seed 0). Two-sided p: permutation of returns within quarter (5,000 permutations).
- **Data:** PitchBook export; returns=excess, lag=1q; 2014Q2..2025Q3, 10 sectors, 447 sector-quarters
- **Result:** estimate -0.0259 (n = 447)
- **95% CI:** [-0.1330, +0.0848]
- **p-value:** 0.7377; BH-adjusted 0.8299
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: 46 quarter clusters.

### P06 - Pooled Spearman rank correlation, deal_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho between deal_growth_qoq in quarter t and the 4Q forward return from the end of t (+lag), pooled over sector-quarters. 95% CI: percentile cluster bootstrap over quarters (10,000 resamples, seed 0). Two-sided p: permutation of returns within quarter (5,000 permutations).
- **Data:** PitchBook export; returns=excess, lag=1q; 2014Q2..2025Q1, 10 sectors, 427 sector-quarters
- **Result:** estimate +0.0142 (n = 427)
- **95% CI:** [-0.0812, +0.1019]
- **p-value:** 0.6981; BH-adjusted 0.8299
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: 44 quarter clusters.

### P07 - Pooled Spearman rank correlation, funding_growth_yoy, 1Q horizon

- **Protocol:** Spearman rho between funding_growth_yoy in quarter t and the 1Q forward return from the end of t (+lag), pooled over sector-quarters. 95% CI: percentile cluster bootstrap over quarters (10,000 resamples, seed 0). Two-sided p: permutation of returns within quarter (5,000 permutations).
- **Data:** PitchBook export; returns=excess, lag=1q; 2015Q1..2025Q4, 10 sectors, 433 sector-quarters
- **Result:** estimate -0.0449 (n = 433)
- **95% CI:** [-0.1468, +0.0551]
- **p-value:** 0.4197; BH-adjusted 0.7555
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: 44 quarter clusters.

### P08 - Pooled Spearman rank correlation, funding_growth_yoy, 2Q horizon

- **Protocol:** Spearman rho between funding_growth_yoy in quarter t and the 2Q forward return from the end of t (+lag), pooled over sector-quarters. 95% CI: percentile cluster bootstrap over quarters (10,000 resamples, seed 0). Two-sided p: permutation of returns within quarter (5,000 permutations).
- **Data:** PitchBook export; returns=excess, lag=1q; 2015Q1..2025Q3, 10 sectors, 423 sector-quarters
- **Result:** estimate -0.0785 (n = 423)
- **95% CI:** [-0.1795, +0.0234]
- **p-value:** 0.1240; BH-adjusted 0.4337
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: 43 quarter clusters.

### P09 - Pooled Spearman rank correlation, funding_growth_yoy, 4Q horizon

- **Protocol:** Spearman rho between funding_growth_yoy in quarter t and the 4Q forward return from the end of t (+lag), pooled over sector-quarters. 95% CI: percentile cluster bootstrap over quarters (10,000 resamples, seed 0). Two-sided p: permutation of returns within quarter (5,000 permutations).
- **Data:** PitchBook export; returns=excess, lag=1q; 2015Q1..2025Q1, 10 sectors, 403 sector-quarters
- **Result:** estimate -0.1116 (n = 403)
- **95% CI:** [-0.2094, -0.0149]
- **p-value:** 0.0336; BH-adjusted 0.3023
- **Verdict:** Nominally significant but does NOT survive BH correction (or the CI and the permutation test disagree). No claim.
- Note: 41 quarter clusters.

### B-biotech-1q - Per-sector Spearman (biotech), funding_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 1Q forward return within sector 'biotech'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=excess, lag=1q; 2014Q2..2025Q4, 1 sectors, 47 sector-quarters
- **Result:** estimate +0.3934 (n = 47)
- **95% CI:** n/a
- **p-value:** 0.0062; BH-adjusted 0.1860
- **Verdict:** Nominally significant but does NOT survive BH correction (or the CI and the permutation test disagree). No claim.

### B-biotech-2q - Per-sector Spearman (biotech), funding_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 2Q forward return within sector 'biotech'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=excess, lag=1q; 2014Q2..2025Q3, 1 sectors, 46 sector-quarters
- **Result:** estimate +0.2921 (n = 46)
- **95% CI:** n/a
- **p-value:** 0.0476; BH-adjusted 0.7139
- **Verdict:** Nominally significant but does NOT survive BH correction (or the CI and the permutation test disagree). No claim.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-biotech-4q - Per-sector Spearman (biotech), funding_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 4Q forward return within sector 'biotech'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=excess, lag=1q; 2014Q2..2025Q1, 1 sectors, 44 sector-quarters
- **Result:** estimate +0.0837 (n = 44)
- **95% CI:** n/a
- **p-value:** 0.5945; BH-adjusted 0.9238
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-cybersecurity-1q - Per-sector Spearman (cybersecurity), funding_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 1Q forward return within sector 'cybersecurity'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=excess, lag=1q; 2015Q1..2025Q4, 1 sectors, 44 sector-quarters
- **Result:** estimate -0.1790 (n = 44)
- **95% CI:** n/a
- **p-value:** 0.2446; BH-adjusted 0.9238
- **Verdict:** Null: no evidence of an effect at this horizon.

### B-cybersecurity-2q - Per-sector Spearman (cybersecurity), funding_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 2Q forward return within sector 'cybersecurity'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=excess, lag=1q; 2015Q1..2025Q3, 1 sectors, 43 sector-quarters
- **Result:** estimate -0.0580 (n = 43)
- **95% CI:** n/a
- **p-value:** 0.7025; BH-adjusted 0.9238
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-cybersecurity-4q - Per-sector Spearman (cybersecurity), funding_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 4Q forward return within sector 'cybersecurity'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=excess, lag=1q; 2015Q1..2025Q1, 1 sectors, 41 sector-quarters
- **Result:** estimate -0.0598 (n = 41)
- **95% CI:** n/a
- **p-value:** 0.7083; BH-adjusted 0.9238
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-energy-1q - Per-sector Spearman (energy), funding_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 1Q forward return within sector 'energy'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=excess, lag=1q; 2014Q2..2025Q4, 1 sectors, 47 sector-quarters
- **Result:** estimate +0.0633 (n = 47)
- **95% CI:** n/a
- **p-value:** 0.6765; BH-adjusted 0.9238
- **Verdict:** Null: no evidence of an effect at this horizon.

### B-energy-2q - Per-sector Spearman (energy), funding_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 2Q forward return within sector 'energy'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=excess, lag=1q; 2014Q2..2025Q3, 1 sectors, 46 sector-quarters
- **Result:** estimate +0.0665 (n = 46)
- **95% CI:** n/a
- **p-value:** 0.6547; BH-adjusted 0.9238
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-energy-4q - Per-sector Spearman (energy), funding_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 4Q forward return within sector 'energy'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=excess, lag=1q; 2014Q2..2025Q1, 1 sectors, 44 sector-quarters
- **Result:** estimate +0.0265 (n = 44)
- **95% CI:** n/a
- **p-value:** 0.8706; BH-adjusted 0.9785
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-financials-1q - Per-sector Spearman (financials), funding_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 1Q forward return within sector 'financials'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=excess, lag=1q; 2014Q2..2025Q4, 1 sectors, 47 sector-quarters
- **Result:** estimate +0.2381 (n = 47)
- **95% CI:** n/a
- **p-value:** 0.1114; BH-adjusted 0.9088
- **Verdict:** Null: no evidence of an effect at this horizon.

### B-financials-2q - Per-sector Spearman (financials), funding_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 2Q forward return within sector 'financials'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=excess, lag=1q; 2014Q2..2025Q3, 1 sectors, 46 sector-quarters
- **Result:** estimate +0.1248 (n = 46)
- **95% CI:** n/a
- **p-value:** 0.4087; BH-adjusted 0.9238
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-financials-4q - Per-sector Spearman (financials), funding_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 4Q forward return within sector 'financials'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=excess, lag=1q; 2014Q2..2025Q1, 1 sectors, 44 sector-quarters
- **Result:** estimate +0.0782 (n = 44)
- **95% CI:** n/a
- **p-value:** 0.6137; BH-adjusted 0.9238
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-fintech-1q - Per-sector Spearman (fintech), funding_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 1Q forward return within sector 'fintech'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=excess, lag=1q; 2016Q4..2025Q4, 1 sectors, 37 sector-quarters
- **Result:** estimate -0.1970 (n = 37)
- **95% CI:** n/a
- **p-value:** 0.2460; BH-adjusted 0.9238
- **Verdict:** Null: no evidence of an effect at this horizon.

### B-fintech-2q - Per-sector Spearman (fintech), funding_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 2Q forward return within sector 'fintech'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=excess, lag=1q; 2016Q4..2025Q3, 1 sectors, 36 sector-quarters
- **Result:** estimate -0.1027 (n = 36)
- **95% CI:** n/a
- **p-value:** 0.5485; BH-adjusted 0.9238
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-fintech-4q - Per-sector Spearman (fintech), funding_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 4Q forward return within sector 'fintech'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=excess, lag=1q; 2016Q4..2025Q1, 1 sectors, 34 sector-quarters
- **Result:** estimate -0.1731 (n = 34)
- **95% CI:** n/a
- **p-value:** 0.3409; BH-adjusted 0.9238
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-healthcare-1q - Per-sector Spearman (healthcare), funding_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 1Q forward return within sector 'healthcare'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=excess, lag=1q; 2014Q2..2025Q4, 1 sectors, 47 sector-quarters
- **Result:** estimate -0.1512 (n = 47)
- **95% CI:** n/a
- **p-value:** 0.3107; BH-adjusted 0.9238
- **Verdict:** Null: no evidence of an effect at this horizon.

### B-healthcare-2q - Per-sector Spearman (healthcare), funding_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 2Q forward return within sector 'healthcare'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=excess, lag=1q; 2014Q2..2025Q3, 1 sectors, 46 sector-quarters
- **Result:** estimate -0.0012 (n = 46)
- **95% CI:** n/a
- **p-value:** 0.9940; BH-adjusted 0.9956
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-healthcare-4q - Per-sector Spearman (healthcare), funding_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 4Q forward return within sector 'healthcare'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=excess, lag=1q; 2014Q2..2025Q1, 1 sectors, 44 sector-quarters
- **Result:** estimate -0.0365 (n = 44)
- **95% CI:** n/a
- **p-value:** 0.8120; BH-adjusted 0.9785
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-industrials-1q - Per-sector Spearman (industrials), funding_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 1Q forward return within sector 'industrials'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=excess, lag=1q; 2014Q2..2025Q4, 1 sectors, 47 sector-quarters
- **Result:** estimate +0.1189 (n = 47)
- **95% CI:** n/a
- **p-value:** 0.4245; BH-adjusted 0.9238
- **Verdict:** Null: no evidence of an effect at this horizon.

### B-industrials-2q - Per-sector Spearman (industrials), funding_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 2Q forward return within sector 'industrials'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=excess, lag=1q; 2014Q2..2025Q3, 1 sectors, 46 sector-quarters
- **Result:** estimate -0.0974 (n = 46)
- **95% CI:** n/a
- **p-value:** 0.5163; BH-adjusted 0.9238
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-industrials-4q - Per-sector Spearman (industrials), funding_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 4Q forward return within sector 'industrials'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=excess, lag=1q; 2014Q2..2025Q1, 1 sectors, 44 sector-quarters
- **Result:** estimate -0.1369 (n = 44)
- **95% CI:** n/a
- **p-value:** 0.3719; BH-adjusted 0.9238
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-semiconductors-1q - Per-sector Spearman (semiconductors), funding_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 1Q forward return within sector 'semiconductors'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=excess, lag=1q; 2014Q2..2025Q4, 1 sectors, 47 sector-quarters
- **Result:** estimate +0.0296 (n = 47)
- **95% CI:** n/a
- **p-value:** 0.8470; BH-adjusted 0.9785
- **Verdict:** Null: no evidence of an effect at this horizon.

### B-semiconductors-2q - Per-sector Spearman (semiconductors), funding_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 2Q forward return within sector 'semiconductors'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=excess, lag=1q; 2014Q2..2025Q3, 1 sectors, 46 sector-quarters
- **Result:** estimate -0.0096 (n = 46)
- **95% CI:** n/a
- **p-value:** 0.9552; BH-adjusted 0.9956
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-semiconductors-4q - Per-sector Spearman (semiconductors), funding_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 4Q forward return within sector 'semiconductors'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=excess, lag=1q; 2014Q2..2025Q1, 1 sectors, 44 sector-quarters
- **Result:** estimate +0.0007 (n = 44)
- **95% CI:** n/a
- **p-value:** 0.9956; BH-adjusted 0.9956
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-software-1q - Per-sector Spearman (software), funding_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 1Q forward return within sector 'software'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=excess, lag=1q; 2014Q2..2025Q4, 1 sectors, 47 sector-quarters
- **Result:** estimate +0.0237 (n = 47)
- **95% CI:** n/a
- **p-value:** 0.8806; BH-adjusted 0.9785
- **Verdict:** Null: no evidence of an effect at this horizon.

### B-software-2q - Per-sector Spearman (software), funding_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 2Q forward return within sector 'software'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=excess, lag=1q; 2014Q2..2025Q3, 1 sectors, 46 sector-quarters
- **Result:** estimate -0.0901 (n = 46)
- **95% CI:** n/a
- **p-value:** 0.5389; BH-adjusted 0.9238
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-software-4q - Per-sector Spearman (software), funding_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 4Q forward return within sector 'software'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=excess, lag=1q; 2014Q2..2025Q1, 1 sectors, 44 sector-quarters
- **Result:** estimate -0.2392 (n = 44)
- **95% CI:** n/a
- **p-value:** 0.1212; BH-adjusted 0.9088
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-technology-1q - Per-sector Spearman (technology), funding_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 1Q forward return within sector 'technology'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=excess, lag=1q; 2014Q2..2025Q4, 1 sectors, 47 sector-quarters
- **Result:** estimate -0.0861 (n = 47)
- **95% CI:** n/a
- **p-value:** 0.5635; BH-adjusted 0.9238
- **Verdict:** Null: no evidence of an effect at this horizon.

### B-technology-2q - Per-sector Spearman (technology), funding_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 2Q forward return within sector 'technology'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=excess, lag=1q; 2014Q2..2025Q3, 1 sectors, 46 sector-quarters
- **Result:** estimate -0.1007 (n = 46)
- **95% CI:** n/a
- **p-value:** 0.4925; BH-adjusted 0.9238
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-technology-4q - Per-sector Spearman (technology), funding_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 4Q forward return within sector 'technology'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=excess, lag=1q; 2014Q2..2025Q1, 1 sectors, 44 sector-quarters
- **Result:** estimate -0.1122 (n = 44)
- **95% CI:** n/a
- **p-value:** 0.4591; BH-adjusted 0.9238
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### W01 - Walk-forward sign persistence of the tercile spread, funding_growth_qoq, 1Q horizon

- **Protocol:** Expanding-window walk-forward with 4 test folds over the quarterly spread series from S01; first 40% of quarters is the initial training window. Report per-fold train/test mean spread and sign agreement, plus the pooled OOS mean with a block bootstrap CI (block = 1, 10,000 resamples, seed 0).
- **Data:** PitchBook export; returns=excess, lag=1q; 2014Q2..2025Q4, 10 sectors, 457 sector-quarters
- **Result:** estimate +0.0139 (n = 28)
- **95% CI:** [-0.0161, +0.0452]
- **p-value:** n/a
- **Verdict:** Sign agreement in 3/4 folds. OOS CI includes 0. Descriptive: no hypothesis test entered into BH.
- Note: Fold 1: train to 2018Q4 mean +0.0125; test 2019Q1..2020Q3 (n=7) mean +0.0000; agree
- Note: Fold 2: train to 2020Q3 mean +0.0091; test 2020Q4..2022Q2 (n=7) mean +0.0428; agree
- Note: Fold 3: train to 2022Q2 mean +0.0163; test 2022Q3..2024Q1 (n=7) mean -0.0121; DISAGREE
- Note: Fold 4: train to 2024Q1 mean +0.0113; test 2024Q2..2025Q4 (n=7) mean +0.0250; agree

### W02 - Walk-forward sign persistence of the tercile spread, funding_growth_qoq, 2Q horizon

- **Protocol:** Expanding-window walk-forward with 4 test folds over the quarterly spread series from S02; first 40% of quarters is the initial training window. Report per-fold train/test mean spread and sign agreement, plus the pooled OOS mean with a block bootstrap CI (block = 2, 10,000 resamples, seed 0).
- **Data:** PitchBook export; returns=excess, lag=1q; 2014Q2..2025Q3, 10 sectors, 447 sector-quarters
- **Result:** estimate +0.0076 (n = 28)
- **95% CI:** [-0.0293, +0.0432]
- **p-value:** n/a
- **Verdict:** Sign agreement in 2/4 folds. OOS CI includes 0. Descriptive: no hypothesis test entered into BH.
- Note: Fold 1: train to 2018Q3 mean +0.0223; test 2018Q4..2020Q2 (n=7) mean -0.0669; DISAGREE
- Note: Fold 2: train to 2020Q2 mean -0.0027; test 2020Q3..2022Q1 (n=7) mean +0.0480; DISAGREE
- Note: Fold 3: train to 2022Q1 mean +0.0084; test 2022Q2..2023Q4 (n=7) mean +0.0081; agree
- Note: Fold 4: train to 2023Q4 mean +0.0083; test 2024Q1..2025Q3 (n=7) mean +0.0412; agree

### W03 - Walk-forward sign persistence of the tercile spread, funding_growth_qoq, 4Q horizon

- **Protocol:** Expanding-window walk-forward with 4 test folds over the quarterly spread series from S03; first 40% of quarters is the initial training window. Report per-fold train/test mean spread and sign agreement, plus the pooled OOS mean with a block bootstrap CI (block = 4, 10,000 resamples, seed 0).
- **Data:** PitchBook export; returns=excess, lag=1q; 2014Q2..2025Q1, 10 sectors, 427 sector-quarters
- **Result:** estimate -0.0084 (n = 26)
- **95% CI:** [-0.0499, +0.0322]
- **p-value:** n/a
- **Verdict:** Sign agreement in 3/4 folds. OOS CI includes 0. Descriptive: no hypothesis test entered into BH.
- Note: Fold 1: train to 2018Q3 mean -0.0034; test 2018Q4..2020Q1 (n=6) mean -0.0315; agree
- Note: Fold 2: train to 2020Q1 mean -0.0104; test 2020Q2..2021Q4 (n=7) mean +0.0148; DISAGREE
- Note: Fold 3: train to 2021Q4 mean -0.0047; test 2022Q1..2023Q3 (n=7) mean -0.0015; agree
- Note: Fold 4: train to 2023Q3 mean -0.0041; test 2023Q4..2025Q1 (n=6) mean -0.0204; agree
