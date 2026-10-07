# Experiment ledger

Generated 2026-10-06 at commit `1d204db` by `scripts/run_experiments.py`.

## Run configuration

| setting | value |
|---|---|
| synthetic | False |
| private_source | pitchbook_export.csv |
| return_mode | vol_adj |
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
| S01 | sorts | funding_growth_qoq | 1Q | 47 | +0.0531 | [-0.0998, +0.2075] | 0.5305 | 0.6821 | Null: no evidence of an effect at this horizon |
| S02 | sorts | funding_growth_qoq | 2Q | 46 | +0.0627 | [-0.0862, +0.2105] | 0.4697 | 0.6821 | Null: no evidence of an effect at this horizon |
| S03 | sorts | funding_growth_qoq | 4Q | 44 | +0.0207 | [-0.1275, +0.1645] | 0.8240 | 0.8240 | Null: no evidence of an effect at this horizon |
| S04 | sorts | deal_growth_qoq | 1Q | 47 | +0.0563 | [-0.1183, +0.2431] | 0.5067 | 0.6821 | Null: no evidence of an effect at this horizon |
| S05 | sorts | deal_growth_qoq | 2Q | 46 | +0.0881 | [-0.0638, +0.2525] | 0.3077 | 0.6821 | Null: no evidence of an effect at this horizon |
| S06 | sorts | deal_growth_qoq | 4Q | 44 | -0.0285 | [-0.1745, +0.1113] | 0.7654 | 0.8240 | Null: no evidence of an effect at this horizon |
| S07 | sorts | funding_growth_yoy | 1Q | 45 | +0.0669 | [-0.1022, +0.2501] | 0.4335 | 0.6821 | Null: no evidence of an effect at this horizon |
| S08 | sorts | funding_growth_yoy | 2Q | 44 | -0.1124 | [-0.2658, +0.0434] | 0.1876 | 0.6821 | Null: no evidence of an effect at this horizon |
| S09 | sorts | funding_growth_yoy | 4Q | 42 | -0.1417 | [-0.3339, +0.0424] | 0.1404 | 0.6821 | Null: no evidence of an effect at this horizon |
| P01 | pooled | funding_growth_qoq | 1Q | 457 | +0.0170 | [-0.0694, +0.1048] | 0.6997 | 0.7871 | Null: no evidence of an effect at this horizon |
| P02 | pooled | funding_growth_qoq | 2Q | 447 | +0.0805 | [-0.0004, +0.1620] | 0.0558 | 0.1740 | Null: no evidence of an effect at this horizon |
| P03 | pooled | funding_growth_qoq | 4Q | 427 | +0.0305 | [-0.0610, +0.1210] | 0.4991 | 0.6417 | Null: no evidence of an effect at this horizon |
| P04 | pooled | deal_growth_qoq | 1Q | 457 | +0.0372 | [-0.0693, +0.1400] | 0.3767 | 0.6417 | Null: no evidence of an effect at this horizon |
| P05 | pooled | deal_growth_qoq | 2Q | 447 | +0.0688 | [-0.0412, +0.1750] | 0.0462 | 0.1740 | Nominally significant but does NOT survive BH correction (or the CI and the permutation test disagree) |
| P06 | pooled | deal_growth_qoq | 4Q | 427 | +0.0061 | [-0.0962, +0.1060] | 0.8708 | 0.8708 | Null: no evidence of an effect at this horizon |
| P07 | pooled | funding_growth_yoy | 1Q | 441 | +0.0718 | [-0.0232, +0.1648] | 0.0580 | 0.1740 | Null: no evidence of an effect at this horizon |
| P08 | pooled | funding_growth_yoy | 2Q | 431 | +0.0303 | [-0.0651, +0.1229] | 0.4411 | 0.6417 | Null: no evidence of an effect at this horizon |
| P09 | pooled | funding_growth_yoy | 4Q | 411 | -0.0538 | [-0.1556, +0.0509] | 0.2531 | 0.5696 | Null: no evidence of an effect at this horizon |
| B-biotech-1q | by_sector | funding_growth_qoq | 1Q | 47 | -0.0686 | n/a | 0.6449 | 0.9682 | Null: no evidence of an effect at this horizon |
| B-biotech-2q | by_sector | funding_growth_qoq | 2Q | 46 | +0.2763 | n/a | 0.0640 | 0.6809 | Null: no evidence of an effect at this horizon |
| B-biotech-4q | by_sector | funding_growth_qoq | 4Q | 44 | +0.0459 | n/a | 0.7796 | 0.9682 | Null: no evidence of an effect at this horizon |
| B-cybersecurity-1q | by_sector | funding_growth_qoq | 1Q | 44 | +0.0038 | n/a | 0.9756 | 0.9954 | Null: no evidence of an effect at this horizon |
| B-cybersecurity-2q | by_sector | funding_growth_qoq | 2Q | 43 | -0.0861 | n/a | 0.5787 | 0.9682 | Null: no evidence of an effect at this horizon |
| B-cybersecurity-4q | by_sector | funding_growth_qoq | 4Q | 41 | +0.0845 | n/a | 0.6013 | 0.9682 | Null: no evidence of an effect at this horizon |
| B-energy-1q | by_sector | funding_growth_qoq | 1Q | 47 | -0.0378 | n/a | 0.8068 | 0.9682 | Null: no evidence of an effect at this horizon |
| B-energy-2q | by_sector | funding_growth_qoq | 2Q | 46 | +0.0772 | n/a | 0.6133 | 0.9682 | Null: no evidence of an effect at this horizon |
| B-energy-4q | by_sector | funding_growth_qoq | 4Q | 44 | +0.0727 | n/a | 0.6377 | 0.9682 | Null: no evidence of an effect at this horizon |
| B-financials-1q | by_sector | funding_growth_qoq | 1Q | 47 | +0.0843 | n/a | 0.5715 | 0.9682 | Null: no evidence of an effect at this horizon |
| B-financials-2q | by_sector | funding_growth_qoq | 2Q | 46 | +0.2606 | n/a | 0.0808 | 0.6809 | Null: no evidence of an effect at this horizon |
| B-financials-4q | by_sector | funding_growth_qoq | 4Q | 44 | +0.2644 | n/a | 0.0908 | 0.6809 | Null: no evidence of an effect at this horizon |
| B-fintech-1q | by_sector | funding_growth_qoq | 1Q | 37 | +0.0012 | n/a | 0.9954 | 0.9954 | Null: no evidence of an effect at this horizon |
| B-fintech-2q | by_sector | funding_growth_qoq | 2Q | 36 | -0.0762 | n/a | 0.6639 | 0.9682 | Null: no evidence of an effect at this horizon |
| B-fintech-4q | by_sector | funding_growth_qoq | 4Q | 34 | +0.0808 | n/a | 0.6417 | 0.9682 | Null: no evidence of an effect at this horizon |
| B-healthcare-1q | by_sector | funding_growth_qoq | 1Q | 47 | -0.0530 | n/a | 0.7257 | 0.9682 | Null: no evidence of an effect at this horizon |
| B-healthcare-2q | by_sector | funding_growth_qoq | 2Q | 46 | -0.0705 | n/a | 0.6349 | 0.9682 | Null: no evidence of an effect at this horizon |
| B-healthcare-4q | by_sector | funding_growth_qoq | 4Q | 44 | +0.0127 | n/a | 0.9310 | 0.9954 | Null: no evidence of an effect at this horizon |
| B-industrials-1q | by_sector | funding_growth_qoq | 1Q | 47 | +0.0221 | n/a | 0.8806 | 0.9954 | Null: no evidence of an effect at this horizon |
| B-industrials-2q | by_sector | funding_growth_qoq | 2Q | 46 | +0.0635 | n/a | 0.6733 | 0.9682 | Null: no evidence of an effect at this horizon |
| B-industrials-4q | by_sector | funding_growth_qoq | 4Q | 44 | +0.0987 | n/a | 0.5287 | 0.9682 | Null: no evidence of an effect at this horizon |
| B-semiconductors-1q | by_sector | funding_growth_qoq | 1Q | 47 | +0.0454 | n/a | 0.7714 | 0.9682 | Null: no evidence of an effect at this horizon |
| B-semiconductors-2q | by_sector | funding_growth_qoq | 2Q | 46 | +0.0191 | n/a | 0.8982 | 0.9954 | Null: no evidence of an effect at this horizon |
| B-semiconductors-4q | by_sector | funding_growth_qoq | 4Q | 44 | -0.0994 | n/a | 0.5111 | 0.9682 | Null: no evidence of an effect at this horizon |
| B-software-1q | by_sector | funding_growth_qoq | 1Q | 47 | +0.1111 | n/a | 0.4505 | 0.9682 | Null: no evidence of an effect at this horizon |
| B-software-2q | by_sector | funding_growth_qoq | 2Q | 46 | +0.1191 | n/a | 0.4185 | 0.9682 | Null: no evidence of an effect at this horizon |
| B-software-4q | by_sector | funding_growth_qoq | 4Q | 44 | -0.1385 | n/a | 0.3697 | 0.9682 | Null: no evidence of an effect at this horizon |
| B-technology-1q | by_sector | funding_growth_qoq | 1Q | 47 | +0.1163 | n/a | 0.4271 | 0.9682 | Null: no evidence of an effect at this horizon |
| B-technology-2q | by_sector | funding_growth_qoq | 2Q | 46 | -0.0479 | n/a | 0.7520 | 0.9682 | Null: no evidence of an effect at this horizon |
| B-technology-4q | by_sector | funding_growth_qoq | 4Q | 44 | -0.3243 | n/a | 0.0380 | 0.6809 | Nominally significant but does NOT survive BH correction (or the CI and the permutation test disagree) |
| W01 | walk_forward | funding_growth_qoq | 1Q | 28 | +0.1342 | [-0.0775, +0.3579] | n/a | n/a | Sign agreement in 2/4 folds |
| W02 | walk_forward | funding_growth_qoq | 2Q | 28 | +0.1252 | [-0.0604, +0.3146] | n/a | n/a | Sign agreement in 1/4 folds |
| W03 | walk_forward | funding_growth_qoq | 4Q | 26 | +0.0785 | [-0.1299, +0.2730] | n/a | n/a | Sign agreement in 1/4 folds |

**48 hypothesis tests run; 0 survive Benjamini-Hochberg at q = 0.05 within their family.**

## Entries

### S01 - Cross-sectional tercile sort (top third minus bottom third), funding_growth_qoq, 1Q horizon

- **Protocol:** Each quarter rank sectors by funding_growth_qoq; long the top third, short the bottom third (k = n//3, min 6 sectors); hold 1Q. Statistic: mean quarterly spread (sigma). 95% CI: paired-by-quarter circular block bootstrap, block = 1 quarters (10,000 resamples, seed 0). Two-sided p: within-quarter permutation of returns (5,000 permutations).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2014Q3..2026Q1, 10 sectors, 457 sector-quarters
- **Result:** estimate +0.0531 (n = 47)
- **95% CI:** [-0.0998, +0.2075]
- **p-value:** 0.5305; BH-adjusted 0.6821
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Mean top-third sigma +0.0222, bottom-third -0.0309; hit rate (spread > 0) 51% of 47 quarters.

### S02 - Cross-sectional tercile sort (top third minus bottom third), funding_growth_qoq, 2Q horizon

- **Protocol:** Each quarter rank sectors by funding_growth_qoq; long the top third, short the bottom third (k = n//3, min 6 sectors); hold 2Q. Statistic: mean quarterly spread (sigma). 95% CI: paired-by-quarter circular block bootstrap, block = 2 quarters (10,000 resamples, seed 0). Two-sided p: within-quarter permutation of returns (5,000 permutations).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2014Q3..2025Q4, 10 sectors, 447 sector-quarters
- **Result:** estimate +0.0627 (n = 46)
- **95% CI:** [-0.0862, +0.2105]
- **p-value:** 0.4697; BH-adjusted 0.6821
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Mean top-third sigma +0.0226, bottom-third -0.0400; hit rate (spread > 0) 61% of 46 quarters.

### S03 - Cross-sectional tercile sort (top third minus bottom third), funding_growth_qoq, 4Q horizon

- **Protocol:** Each quarter rank sectors by funding_growth_qoq; long the top third, short the bottom third (k = n//3, min 6 sectors); hold 4Q. Statistic: mean quarterly spread (sigma). 95% CI: paired-by-quarter circular block bootstrap, block = 4 quarters (10,000 resamples, seed 0). Two-sided p: within-quarter permutation of returns (5,000 permutations).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2014Q3..2025Q2, 10 sectors, 427 sector-quarters
- **Result:** estimate +0.0207 (n = 44)
- **95% CI:** [-0.1275, +0.1645]
- **p-value:** 0.8240; BH-adjusted 0.8240
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Mean top-third sigma -0.0183, bottom-third -0.0391; hit rate (spread > 0) 57% of 44 quarters.

### S04 - Cross-sectional tercile sort (top third minus bottom third), deal_growth_qoq, 1Q horizon

- **Protocol:** Each quarter rank sectors by deal_growth_qoq; long the top third, short the bottom third (k = n//3, min 6 sectors); hold 1Q. Statistic: mean quarterly spread (sigma). 95% CI: paired-by-quarter circular block bootstrap, block = 1 quarters (10,000 resamples, seed 0). Two-sided p: within-quarter permutation of returns (5,000 permutations).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2014Q3..2026Q1, 10 sectors, 457 sector-quarters
- **Result:** estimate +0.0563 (n = 47)
- **95% CI:** [-0.1183, +0.2431]
- **p-value:** 0.5067; BH-adjusted 0.6821
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Mean top-third sigma +0.0416, bottom-third -0.0147; hit rate (spread > 0) 60% of 47 quarters.

### S05 - Cross-sectional tercile sort (top third minus bottom third), deal_growth_qoq, 2Q horizon

- **Protocol:** Each quarter rank sectors by deal_growth_qoq; long the top third, short the bottom third (k = n//3, min 6 sectors); hold 2Q. Statistic: mean quarterly spread (sigma). 95% CI: paired-by-quarter circular block bootstrap, block = 2 quarters (10,000 resamples, seed 0). Two-sided p: within-quarter permutation of returns (5,000 permutations).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2014Q3..2025Q4, 10 sectors, 447 sector-quarters
- **Result:** estimate +0.0881 (n = 46)
- **95% CI:** [-0.0638, +0.2525]
- **p-value:** 0.3077; BH-adjusted 0.6821
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Mean top-third sigma +0.0212, bottom-third -0.0669; hit rate (spread > 0) 52% of 46 quarters.

### S06 - Cross-sectional tercile sort (top third minus bottom third), deal_growth_qoq, 4Q horizon

- **Protocol:** Each quarter rank sectors by deal_growth_qoq; long the top third, short the bottom third (k = n//3, min 6 sectors); hold 4Q. Statistic: mean quarterly spread (sigma). 95% CI: paired-by-quarter circular block bootstrap, block = 4 quarters (10,000 resamples, seed 0). Two-sided p: within-quarter permutation of returns (5,000 permutations).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2014Q3..2025Q2, 10 sectors, 427 sector-quarters
- **Result:** estimate -0.0285 (n = 44)
- **95% CI:** [-0.1745, +0.1113]
- **p-value:** 0.7654; BH-adjusted 0.8240
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Mean top-third sigma -0.0510, bottom-third -0.0225; hit rate (spread > 0) 48% of 44 quarters.

### S07 - Cross-sectional tercile sort (top third minus bottom third), funding_growth_yoy, 1Q horizon

- **Protocol:** Each quarter rank sectors by funding_growth_yoy; long the top third, short the bottom third (k = n//3, min 6 sectors); hold 1Q. Statistic: mean quarterly spread (sigma). 95% CI: paired-by-quarter circular block bootstrap, block = 1 quarters (10,000 resamples, seed 0). Two-sided p: within-quarter permutation of returns (5,000 permutations).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2015Q1..2026Q1, 10 sectors, 441 sector-quarters
- **Result:** estimate +0.0669 (n = 45)
- **95% CI:** [-0.1022, +0.2501]
- **p-value:** 0.4335; BH-adjusted 0.6821
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Mean top-third sigma -0.0021, bottom-third -0.0690; hit rate (spread > 0) 44% of 45 quarters.

### S08 - Cross-sectional tercile sort (top third minus bottom third), funding_growth_yoy, 2Q horizon

- **Protocol:** Each quarter rank sectors by funding_growth_yoy; long the top third, short the bottom third (k = n//3, min 6 sectors); hold 2Q. Statistic: mean quarterly spread (sigma). 95% CI: paired-by-quarter circular block bootstrap, block = 2 quarters (10,000 resamples, seed 0). Two-sided p: within-quarter permutation of returns (5,000 permutations).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2015Q1..2025Q4, 10 sectors, 431 sector-quarters
- **Result:** estimate -0.1124 (n = 44)
- **95% CI:** [-0.2658, +0.0434]
- **p-value:** 0.1876; BH-adjusted 0.6821
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Mean top-third sigma -0.0937, bottom-third +0.0186; hit rate (spread > 0) 41% of 44 quarters.

### S09 - Cross-sectional tercile sort (top third minus bottom third), funding_growth_yoy, 4Q horizon

- **Protocol:** Each quarter rank sectors by funding_growth_yoy; long the top third, short the bottom third (k = n//3, min 6 sectors); hold 4Q. Statistic: mean quarterly spread (sigma). 95% CI: paired-by-quarter circular block bootstrap, block = 4 quarters (10,000 resamples, seed 0). Two-sided p: within-quarter permutation of returns (5,000 permutations).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2015Q1..2025Q2, 10 sectors, 411 sector-quarters
- **Result:** estimate -0.1417 (n = 42)
- **95% CI:** [-0.3339, +0.0424]
- **p-value:** 0.1404; BH-adjusted 0.6821
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Mean top-third sigma -0.1324, bottom-third +0.0093; hit rate (spread > 0) 38% of 42 quarters.

### P01 - Pooled Spearman rank correlation, funding_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho between funding_growth_qoq in quarter t and the 1Q forward return from the end of t (+lag), pooled over sector-quarters. 95% CI: percentile cluster bootstrap over quarters (10,000 resamples, seed 0). Two-sided p: permutation of returns within quarter (5,000 permutations).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2014Q3..2026Q1, 10 sectors, 457 sector-quarters
- **Result:** estimate +0.0170 (n = 457)
- **95% CI:** [-0.0694, +0.1048]
- **p-value:** 0.6997; BH-adjusted 0.7871
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: 47 quarter clusters.

### P02 - Pooled Spearman rank correlation, funding_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho between funding_growth_qoq in quarter t and the 2Q forward return from the end of t (+lag), pooled over sector-quarters. 95% CI: percentile cluster bootstrap over quarters (10,000 resamples, seed 0). Two-sided p: permutation of returns within quarter (5,000 permutations).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2014Q3..2025Q4, 10 sectors, 447 sector-quarters
- **Result:** estimate +0.0805 (n = 447)
- **95% CI:** [-0.0004, +0.1620]
- **p-value:** 0.0558; BH-adjusted 0.1740
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: 46 quarter clusters.

### P03 - Pooled Spearman rank correlation, funding_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho between funding_growth_qoq in quarter t and the 4Q forward return from the end of t (+lag), pooled over sector-quarters. 95% CI: percentile cluster bootstrap over quarters (10,000 resamples, seed 0). Two-sided p: permutation of returns within quarter (5,000 permutations).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2014Q3..2025Q2, 10 sectors, 427 sector-quarters
- **Result:** estimate +0.0305 (n = 427)
- **95% CI:** [-0.0610, +0.1210]
- **p-value:** 0.4991; BH-adjusted 0.6417
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: 44 quarter clusters.

### P04 - Pooled Spearman rank correlation, deal_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho between deal_growth_qoq in quarter t and the 1Q forward return from the end of t (+lag), pooled over sector-quarters. 95% CI: percentile cluster bootstrap over quarters (10,000 resamples, seed 0). Two-sided p: permutation of returns within quarter (5,000 permutations).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2014Q3..2026Q1, 10 sectors, 457 sector-quarters
- **Result:** estimate +0.0372 (n = 457)
- **95% CI:** [-0.0693, +0.1400]
- **p-value:** 0.3767; BH-adjusted 0.6417
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: 47 quarter clusters.

### P05 - Pooled Spearman rank correlation, deal_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho between deal_growth_qoq in quarter t and the 2Q forward return from the end of t (+lag), pooled over sector-quarters. 95% CI: percentile cluster bootstrap over quarters (10,000 resamples, seed 0). Two-sided p: permutation of returns within quarter (5,000 permutations).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2014Q3..2025Q4, 10 sectors, 447 sector-quarters
- **Result:** estimate +0.0688 (n = 447)
- **95% CI:** [-0.0412, +0.1750]
- **p-value:** 0.0462; BH-adjusted 0.1740
- **Verdict:** Nominally significant but does NOT survive BH correction (or the CI and the permutation test disagree). No claim.
- Note: 46 quarter clusters.

### P06 - Pooled Spearman rank correlation, deal_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho between deal_growth_qoq in quarter t and the 4Q forward return from the end of t (+lag), pooled over sector-quarters. 95% CI: percentile cluster bootstrap over quarters (10,000 resamples, seed 0). Two-sided p: permutation of returns within quarter (5,000 permutations).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2014Q3..2025Q2, 10 sectors, 427 sector-quarters
- **Result:** estimate +0.0061 (n = 427)
- **95% CI:** [-0.0962, +0.1060]
- **p-value:** 0.8708; BH-adjusted 0.8708
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: 44 quarter clusters.

### P07 - Pooled Spearman rank correlation, funding_growth_yoy, 1Q horizon

- **Protocol:** Spearman rho between funding_growth_yoy in quarter t and the 1Q forward return from the end of t (+lag), pooled over sector-quarters. 95% CI: percentile cluster bootstrap over quarters (10,000 resamples, seed 0). Two-sided p: permutation of returns within quarter (5,000 permutations).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2015Q1..2026Q1, 10 sectors, 441 sector-quarters
- **Result:** estimate +0.0718 (n = 441)
- **95% CI:** [-0.0232, +0.1648]
- **p-value:** 0.0580; BH-adjusted 0.1740
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: 45 quarter clusters.

### P08 - Pooled Spearman rank correlation, funding_growth_yoy, 2Q horizon

- **Protocol:** Spearman rho between funding_growth_yoy in quarter t and the 2Q forward return from the end of t (+lag), pooled over sector-quarters. 95% CI: percentile cluster bootstrap over quarters (10,000 resamples, seed 0). Two-sided p: permutation of returns within quarter (5,000 permutations).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2015Q1..2025Q4, 10 sectors, 431 sector-quarters
- **Result:** estimate +0.0303 (n = 431)
- **95% CI:** [-0.0651, +0.1229]
- **p-value:** 0.4411; BH-adjusted 0.6417
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: 44 quarter clusters.

### P09 - Pooled Spearman rank correlation, funding_growth_yoy, 4Q horizon

- **Protocol:** Spearman rho between funding_growth_yoy in quarter t and the 4Q forward return from the end of t (+lag), pooled over sector-quarters. 95% CI: percentile cluster bootstrap over quarters (10,000 resamples, seed 0). Two-sided p: permutation of returns within quarter (5,000 permutations).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2015Q1..2025Q2, 10 sectors, 411 sector-quarters
- **Result:** estimate -0.0538 (n = 411)
- **95% CI:** [-0.1556, +0.0509]
- **p-value:** 0.2531; BH-adjusted 0.5696
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: 42 quarter clusters.

### B-biotech-1q - Per-sector Spearman (biotech), funding_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 1Q forward return within sector 'biotech'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2014Q3..2026Q1, 1 sectors, 47 sector-quarters
- **Result:** estimate -0.0686 (n = 47)
- **95% CI:** n/a
- **p-value:** 0.6449; BH-adjusted 0.9682
- **Verdict:** Null: no evidence of an effect at this horizon.

### B-biotech-2q - Per-sector Spearman (biotech), funding_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 2Q forward return within sector 'biotech'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2014Q3..2025Q4, 1 sectors, 46 sector-quarters
- **Result:** estimate +0.2763 (n = 46)
- **95% CI:** n/a
- **p-value:** 0.0640; BH-adjusted 0.6809
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-biotech-4q - Per-sector Spearman (biotech), funding_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 4Q forward return within sector 'biotech'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2014Q3..2025Q2, 1 sectors, 44 sector-quarters
- **Result:** estimate +0.0459 (n = 44)
- **95% CI:** n/a
- **p-value:** 0.7796; BH-adjusted 0.9682
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-cybersecurity-1q - Per-sector Spearman (cybersecurity), funding_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 1Q forward return within sector 'cybersecurity'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2015Q2..2026Q1, 1 sectors, 44 sector-quarters
- **Result:** estimate +0.0038 (n = 44)
- **95% CI:** n/a
- **p-value:** 0.9756; BH-adjusted 0.9954
- **Verdict:** Null: no evidence of an effect at this horizon.

### B-cybersecurity-2q - Per-sector Spearman (cybersecurity), funding_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 2Q forward return within sector 'cybersecurity'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2015Q2..2025Q4, 1 sectors, 43 sector-quarters
- **Result:** estimate -0.0861 (n = 43)
- **95% CI:** n/a
- **p-value:** 0.5787; BH-adjusted 0.9682
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-cybersecurity-4q - Per-sector Spearman (cybersecurity), funding_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 4Q forward return within sector 'cybersecurity'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2015Q2..2025Q2, 1 sectors, 41 sector-quarters
- **Result:** estimate +0.0845 (n = 41)
- **95% CI:** n/a
- **p-value:** 0.6013; BH-adjusted 0.9682
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-energy-1q - Per-sector Spearman (energy), funding_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 1Q forward return within sector 'energy'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2014Q3..2026Q1, 1 sectors, 47 sector-quarters
- **Result:** estimate -0.0378 (n = 47)
- **95% CI:** n/a
- **p-value:** 0.8068; BH-adjusted 0.9682
- **Verdict:** Null: no evidence of an effect at this horizon.

### B-energy-2q - Per-sector Spearman (energy), funding_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 2Q forward return within sector 'energy'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2014Q3..2025Q4, 1 sectors, 46 sector-quarters
- **Result:** estimate +0.0772 (n = 46)
- **95% CI:** n/a
- **p-value:** 0.6133; BH-adjusted 0.9682
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-energy-4q - Per-sector Spearman (energy), funding_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 4Q forward return within sector 'energy'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2014Q3..2025Q2, 1 sectors, 44 sector-quarters
- **Result:** estimate +0.0727 (n = 44)
- **95% CI:** n/a
- **p-value:** 0.6377; BH-adjusted 0.9682
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-financials-1q - Per-sector Spearman (financials), funding_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 1Q forward return within sector 'financials'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2014Q3..2026Q1, 1 sectors, 47 sector-quarters
- **Result:** estimate +0.0843 (n = 47)
- **95% CI:** n/a
- **p-value:** 0.5715; BH-adjusted 0.9682
- **Verdict:** Null: no evidence of an effect at this horizon.

### B-financials-2q - Per-sector Spearman (financials), funding_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 2Q forward return within sector 'financials'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2014Q3..2025Q4, 1 sectors, 46 sector-quarters
- **Result:** estimate +0.2606 (n = 46)
- **95% CI:** n/a
- **p-value:** 0.0808; BH-adjusted 0.6809
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-financials-4q - Per-sector Spearman (financials), funding_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 4Q forward return within sector 'financials'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2014Q3..2025Q2, 1 sectors, 44 sector-quarters
- **Result:** estimate +0.2644 (n = 44)
- **95% CI:** n/a
- **p-value:** 0.0908; BH-adjusted 0.6809
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-fintech-1q - Per-sector Spearman (fintech), funding_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 1Q forward return within sector 'fintech'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2017Q1..2026Q1, 1 sectors, 37 sector-quarters
- **Result:** estimate +0.0012 (n = 37)
- **95% CI:** n/a
- **p-value:** 0.9954; BH-adjusted 0.9954
- **Verdict:** Null: no evidence of an effect at this horizon.

### B-fintech-2q - Per-sector Spearman (fintech), funding_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 2Q forward return within sector 'fintech'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2017Q1..2025Q4, 1 sectors, 36 sector-quarters
- **Result:** estimate -0.0762 (n = 36)
- **95% CI:** n/a
- **p-value:** 0.6639; BH-adjusted 0.9682
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-fintech-4q - Per-sector Spearman (fintech), funding_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 4Q forward return within sector 'fintech'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2017Q1..2025Q2, 1 sectors, 34 sector-quarters
- **Result:** estimate +0.0808 (n = 34)
- **95% CI:** n/a
- **p-value:** 0.6417; BH-adjusted 0.9682
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-healthcare-1q - Per-sector Spearman (healthcare), funding_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 1Q forward return within sector 'healthcare'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2014Q3..2026Q1, 1 sectors, 47 sector-quarters
- **Result:** estimate -0.0530 (n = 47)
- **95% CI:** n/a
- **p-value:** 0.7257; BH-adjusted 0.9682
- **Verdict:** Null: no evidence of an effect at this horizon.

### B-healthcare-2q - Per-sector Spearman (healthcare), funding_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 2Q forward return within sector 'healthcare'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2014Q3..2025Q4, 1 sectors, 46 sector-quarters
- **Result:** estimate -0.0705 (n = 46)
- **95% CI:** n/a
- **p-value:** 0.6349; BH-adjusted 0.9682
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-healthcare-4q - Per-sector Spearman (healthcare), funding_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 4Q forward return within sector 'healthcare'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2014Q3..2025Q2, 1 sectors, 44 sector-quarters
- **Result:** estimate +0.0127 (n = 44)
- **95% CI:** n/a
- **p-value:** 0.9310; BH-adjusted 0.9954
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-industrials-1q - Per-sector Spearman (industrials), funding_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 1Q forward return within sector 'industrials'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2014Q3..2026Q1, 1 sectors, 47 sector-quarters
- **Result:** estimate +0.0221 (n = 47)
- **95% CI:** n/a
- **p-value:** 0.8806; BH-adjusted 0.9954
- **Verdict:** Null: no evidence of an effect at this horizon.

### B-industrials-2q - Per-sector Spearman (industrials), funding_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 2Q forward return within sector 'industrials'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2014Q3..2025Q4, 1 sectors, 46 sector-quarters
- **Result:** estimate +0.0635 (n = 46)
- **95% CI:** n/a
- **p-value:** 0.6733; BH-adjusted 0.9682
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-industrials-4q - Per-sector Spearman (industrials), funding_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 4Q forward return within sector 'industrials'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2014Q3..2025Q2, 1 sectors, 44 sector-quarters
- **Result:** estimate +0.0987 (n = 44)
- **95% CI:** n/a
- **p-value:** 0.5287; BH-adjusted 0.9682
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-semiconductors-1q - Per-sector Spearman (semiconductors), funding_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 1Q forward return within sector 'semiconductors'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2014Q3..2026Q1, 1 sectors, 47 sector-quarters
- **Result:** estimate +0.0454 (n = 47)
- **95% CI:** n/a
- **p-value:** 0.7714; BH-adjusted 0.9682
- **Verdict:** Null: no evidence of an effect at this horizon.

### B-semiconductors-2q - Per-sector Spearman (semiconductors), funding_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 2Q forward return within sector 'semiconductors'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2014Q3..2025Q4, 1 sectors, 46 sector-quarters
- **Result:** estimate +0.0191 (n = 46)
- **95% CI:** n/a
- **p-value:** 0.8982; BH-adjusted 0.9954
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-semiconductors-4q - Per-sector Spearman (semiconductors), funding_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 4Q forward return within sector 'semiconductors'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2014Q3..2025Q2, 1 sectors, 44 sector-quarters
- **Result:** estimate -0.0994 (n = 44)
- **95% CI:** n/a
- **p-value:** 0.5111; BH-adjusted 0.9682
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-software-1q - Per-sector Spearman (software), funding_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 1Q forward return within sector 'software'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2014Q3..2026Q1, 1 sectors, 47 sector-quarters
- **Result:** estimate +0.1111 (n = 47)
- **95% CI:** n/a
- **p-value:** 0.4505; BH-adjusted 0.9682
- **Verdict:** Null: no evidence of an effect at this horizon.

### B-software-2q - Per-sector Spearman (software), funding_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 2Q forward return within sector 'software'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2014Q3..2025Q4, 1 sectors, 46 sector-quarters
- **Result:** estimate +0.1191 (n = 46)
- **95% CI:** n/a
- **p-value:** 0.4185; BH-adjusted 0.9682
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-software-4q - Per-sector Spearman (software), funding_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 4Q forward return within sector 'software'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2014Q3..2025Q2, 1 sectors, 44 sector-quarters
- **Result:** estimate -0.1385 (n = 44)
- **95% CI:** n/a
- **p-value:** 0.3697; BH-adjusted 0.9682
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-technology-1q - Per-sector Spearman (technology), funding_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 1Q forward return within sector 'technology'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2014Q3..2026Q1, 1 sectors, 47 sector-quarters
- **Result:** estimate +0.1163 (n = 47)
- **95% CI:** n/a
- **p-value:** 0.4271; BH-adjusted 0.9682
- **Verdict:** Null: no evidence of an effect at this horizon.

### B-technology-2q - Per-sector Spearman (technology), funding_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 2Q forward return within sector 'technology'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2014Q3..2025Q4, 1 sectors, 46 sector-quarters
- **Result:** estimate -0.0479 (n = 46)
- **95% CI:** n/a
- **p-value:** 0.7520; BH-adjusted 0.9682
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-technology-4q - Per-sector Spearman (technology), funding_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 4Q forward return within sector 'technology'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2014Q3..2025Q2, 1 sectors, 44 sector-quarters
- **Result:** estimate -0.3243 (n = 44)
- **95% CI:** n/a
- **p-value:** 0.0380; BH-adjusted 0.6809
- **Verdict:** Nominally significant but does NOT survive BH correction (or the CI and the permutation test disagree). No claim.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### W01 - Walk-forward sign persistence of the tercile spread, funding_growth_qoq, 1Q horizon

- **Protocol:** Expanding-window walk-forward with 4 test folds over the quarterly spread series from S01; first 40% of quarters is the initial training window. Report per-fold train/test mean spread and sign agreement, plus the pooled OOS mean with a block bootstrap CI (block = 1, 10,000 resamples, seed 0).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2014Q3..2026Q1, 10 sectors, 457 sector-quarters
- **Result:** estimate +0.1342 (n = 28)
- **95% CI:** [-0.0775, +0.3579]
- **p-value:** n/a
- **Verdict:** Sign agreement in 2/4 folds. OOS CI includes 0. Descriptive: no hypothesis test entered into BH.
- Note: Fold 1: train to 2019Q1 mean -0.0664; test 2019Q2..2020Q4 (n=7) mean +0.0510; DISAGREE
- Note: Fold 2: train to 2020Q4 mean -0.0348; test 2021Q1..2022Q3 (n=7) mean +0.2343; DISAGREE
- Note: Fold 3: train to 2022Q3 mean +0.0223; test 2022Q4..2024Q2 (n=7) mean +0.0954; agree
- Note: Fold 4: train to 2024Q2 mean +0.0350; test 2024Q3..2026Q1 (n=7) mean +0.1564; agree

### W02 - Walk-forward sign persistence of the tercile spread, funding_growth_qoq, 2Q horizon

- **Protocol:** Expanding-window walk-forward with 4 test folds over the quarterly spread series from S02; first 40% of quarters is the initial training window. Report per-fold train/test mean spread and sign agreement, plus the pooled OOS mean with a block bootstrap CI (block = 2, 10,000 resamples, seed 0).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2014Q3..2025Q4, 10 sectors, 447 sector-quarters
- **Result:** estimate +0.1252 (n = 28)
- **95% CI:** [-0.0604, +0.3146]
- **p-value:** n/a
- **Verdict:** Sign agreement in 1/4 folds. OOS CI includes 0. Descriptive: no hypothesis test entered into BH.
- Note: Fold 1: train to 2018Q4 mean -0.0347; test 2019Q1..2020Q3 (n=7) mean +0.0390; DISAGREE
- Note: Fold 2: train to 2020Q3 mean -0.0140; test 2020Q4..2022Q2 (n=7) mean +0.2942; DISAGREE
- Note: Fold 3: train to 2022Q2 mean +0.0534; test 2022Q3..2024Q1 (n=7) mean -0.0185; DISAGREE
- Note: Fold 4: train to 2024Q1 mean +0.0405; test 2024Q2..2025Q4 (n=7) mean +0.1863; agree

### W03 - Walk-forward sign persistence of the tercile spread, funding_growth_qoq, 4Q horizon

- **Protocol:** Expanding-window walk-forward with 4 test folds over the quarterly spread series from S03; first 40% of quarters is the initial training window. Report per-fold train/test mean spread and sign agreement, plus the pooled OOS mean with a block bootstrap CI (block = 4, 10,000 resamples, seed 0).
- **Data:** PitchBook export; returns=vol_adj, lag=0q; 2014Q3..2025Q2, 10 sectors, 427 sector-quarters
- **Result:** estimate +0.0785 (n = 26)
- **95% CI:** [-0.1299, +0.2730]
- **p-value:** n/a
- **Verdict:** Sign agreement in 1/4 folds. OOS CI includes 0. Descriptive: no hypothesis test entered into BH.
- Note: Fold 1: train to 2018Q4 mean -0.0628; test 2019Q1..2020Q2 (n=6) mean -0.3078; agree
- Note: Fold 2: train to 2020Q2 mean -0.1240; test 2020Q3..2022Q1 (n=7) mean +0.1972; DISAGREE
- Note: Fold 3: train to 2022Q1 mean -0.0515; test 2022Q2..2023Q4 (n=7) mean +0.1490; DISAGREE
- Note: Fold 4: train to 2023Q4 mean -0.0145; test 2024Q1..2025Q2 (n=6) mean +0.2439; DISAGREE
