# Experiment ledger

Generated 2026-10-06 at commit `1d204db` by `scripts/run_experiments.py`.

## Run configuration

| setting | value |
|---|---|
| synthetic | False |
| private_source | pitchbook_export.csv |
| return_mode | raw |
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
| S01 | sorts | funding_growth_qoq | 1Q | 48 | +0.0127 | [-0.0063, +0.0324] | 0.2418 | 0.4352 | Null: no evidence of an effect at this horizon |
| S02 | sorts | funding_growth_qoq | 2Q | 47 | +0.0261 | [+0.0005, +0.0532] | 0.0948 | 0.3971 | Nominally significant but does NOT survive BH correction (or the CI and the permutation test disagree) |
| S03 | sorts | funding_growth_qoq | 4Q | 45 | +0.0233 | [-0.0196, +0.0650] | 0.3315 | 0.4561 | Null: no evidence of an effect at this horizon |
| S04 | sorts | deal_growth_qoq | 1Q | 48 | +0.0061 | [-0.0143, +0.0270] | 0.5725 | 0.5725 | Null: no evidence of an effect at this horizon |
| S05 | sorts | deal_growth_qoq | 2Q | 47 | +0.0234 | [-0.0078, +0.0547] | 0.1324 | 0.3971 | Null: no evidence of an effect at this horizon |
| S06 | sorts | deal_growth_qoq | 4Q | 45 | -0.0222 | [-0.0686, +0.0188] | 0.3547 | 0.4561 | Null: no evidence of an effect at this horizon |
| S07 | sorts | funding_growth_yoy | 1Q | 45 | +0.0186 | [-0.0035, +0.0430] | 0.0894 | 0.3971 | Null: no evidence of an effect at this horizon |
| S08 | sorts | funding_growth_yoy | 2Q | 44 | -0.0130 | [-0.0380, +0.0138] | 0.4323 | 0.4864 | Null: no evidence of an effect at this horizon |
| S09 | sorts | funding_growth_yoy | 4Q | 42 | -0.0330 | [-0.0783, +0.0121] | 0.1856 | 0.4175 | Null: no evidence of an effect at this horizon |
| P01 | pooled | funding_growth_qoq | 1Q | 469 | +0.0712 | [-0.0491, +0.1872] | 0.4129 | 0.5903 | Null: no evidence of an effect at this horizon |
| P02 | pooled | funding_growth_qoq | 2Q | 459 | +0.0948 | [-0.0169, +0.2044] | 0.0186 | 0.0837 | Nominally significant but does NOT survive BH correction (or the CI and the permutation test disagree) |
| P03 | pooled | funding_growth_qoq | 4Q | 439 | +0.0244 | [-0.1075, +0.1518] | 0.4933 | 0.5903 | Null: no evidence of an effect at this horizon |
| P04 | pooled | deal_growth_qoq | 1Q | 469 | +0.1106 | [-0.0398, +0.2580] | 0.3815 | 0.5903 | Null: no evidence of an effect at this horizon |
| P05 | pooled | deal_growth_qoq | 2Q | 459 | +0.0781 | [-0.0889, +0.2377] | 0.0132 | 0.0837 | Nominally significant but does NOT survive BH correction (or the CI and the permutation test disagree) |
| P06 | pooled | deal_growth_qoq | 4Q | 439 | -0.0417 | [-0.2101, +0.1274] | 0.5247 | 0.5903 | Null: no evidence of an effect at this horizon |
| P07 | pooled | funding_growth_yoy | 1Q | 444 | +0.0480 | [-0.0913, +0.1883] | 0.0768 | 0.2304 | Null: no evidence of an effect at this horizon |
| P08 | pooled | funding_growth_yoy | 2Q | 434 | -0.0395 | [-0.1579, +0.0775] | 0.6975 | 0.6975 | Null: no evidence of an effect at this horizon |
| P09 | pooled | funding_growth_yoy | 4Q | 414 | -0.1919 | [-0.3327, -0.0470] | 0.1228 | 0.2762 | Nominally significant but does NOT survive BH correction (or the CI and the permutation test disagree) |
| B-biotech-1q | by_sector | funding_growth_qoq | 1Q | 48 | -0.0337 | n/a | 0.8156 | 0.9063 | Null: no evidence of an effect at this horizon |
| B-biotech-2q | by_sector | funding_growth_qoq | 2Q | 47 | +0.2127 | n/a | 0.1528 | 0.9063 | Null: no evidence of an effect at this horizon |
| B-biotech-4q | by_sector | funding_growth_qoq | 4Q | 45 | +0.0046 | n/a | 0.9788 | 0.9810 | Null: no evidence of an effect at this horizon |
| B-cybersecurity-1q | by_sector | funding_growth_qoq | 1Q | 46 | +0.2127 | n/a | 0.1470 | 0.9063 | Null: no evidence of an effect at this horizon |
| B-cybersecurity-2q | by_sector | funding_growth_qoq | 2Q | 45 | +0.0381 | n/a | 0.7922 | 0.9063 | Null: no evidence of an effect at this horizon |
| B-cybersecurity-4q | by_sector | funding_growth_qoq | 4Q | 43 | +0.0835 | n/a | 0.6075 | 0.9063 | Null: no evidence of an effect at this horizon |
| B-energy-1q | by_sector | funding_growth_qoq | 1Q | 48 | +0.0629 | n/a | 0.6667 | 0.9063 | Null: no evidence of an effect at this horizon |
| B-energy-2q | by_sector | funding_growth_qoq | 2Q | 47 | +0.1294 | n/a | 0.3799 | 0.9063 | Null: no evidence of an effect at this horizon |
| B-energy-4q | by_sector | funding_growth_qoq | 4Q | 45 | +0.0719 | n/a | 0.6411 | 0.9063 | Null: no evidence of an effect at this horizon |
| B-financials-1q | by_sector | funding_growth_qoq | 1Q | 48 | +0.0689 | n/a | 0.6457 | 0.9063 | Null: no evidence of an effect at this horizon |
| B-financials-2q | by_sector | funding_growth_qoq | 2Q | 47 | +0.1285 | n/a | 0.3833 | 0.9063 | Null: no evidence of an effect at this horizon |
| B-financials-4q | by_sector | funding_growth_qoq | 4Q | 45 | +0.2134 | n/a | 0.1594 | 0.9063 | Null: no evidence of an effect at this horizon |
| B-fintech-1q | by_sector | funding_growth_qoq | 1Q | 39 | +0.0939 | n/a | 0.5593 | 0.9063 | Null: no evidence of an effect at this horizon |
| B-fintech-2q | by_sector | funding_growth_qoq | 2Q | 38 | -0.0524 | n/a | 0.7419 | 0.9063 | Null: no evidence of an effect at this horizon |
| B-fintech-4q | by_sector | funding_growth_qoq | 4Q | 36 | -0.0571 | n/a | 0.7435 | 0.9063 | Null: no evidence of an effect at this horizon |
| B-healthcare-1q | by_sector | funding_growth_qoq | 1Q | 48 | -0.0601 | n/a | 0.6825 | 0.9063 | Null: no evidence of an effect at this horizon |
| B-healthcare-2q | by_sector | funding_growth_qoq | 2Q | 47 | -0.0820 | n/a | 0.5699 | 0.9063 | Null: no evidence of an effect at this horizon |
| B-healthcare-4q | by_sector | funding_growth_qoq | 4Q | 45 | +0.0399 | n/a | 0.7924 | 0.9063 | Null: no evidence of an effect at this horizon |
| B-industrials-1q | by_sector | funding_growth_qoq | 1Q | 48 | -0.0144 | n/a | 0.9230 | 0.9810 | Null: no evidence of an effect at this horizon |
| B-industrials-2q | by_sector | funding_growth_qoq | 2Q | 47 | +0.0371 | n/a | 0.8026 | 0.9063 | Null: no evidence of an effect at this horizon |
| B-industrials-4q | by_sector | funding_growth_qoq | 4Q | 45 | +0.0626 | n/a | 0.6767 | 0.9063 | Null: no evidence of an effect at this horizon |
| B-semiconductors-1q | by_sector | funding_growth_qoq | 1Q | 48 | -0.0728 | n/a | 0.6237 | 0.9063 | Null: no evidence of an effect at this horizon |
| B-semiconductors-2q | by_sector | funding_growth_qoq | 2Q | 47 | +0.0537 | n/a | 0.7283 | 0.9063 | Null: no evidence of an effect at this horizon |
| B-semiconductors-4q | by_sector | funding_growth_qoq | 4Q | 45 | +0.0038 | n/a | 0.9810 | 0.9810 | Null: no evidence of an effect at this horizon |
| B-software-1q | by_sector | funding_growth_qoq | 1Q | 48 | +0.2670 | n/a | 0.0666 | 0.9063 | Null: no evidence of an effect at this horizon |
| B-software-2q | by_sector | funding_growth_qoq | 2Q | 47 | +0.1643 | n/a | 0.2649 | 0.9063 | Null: no evidence of an effect at this horizon |
| B-software-4q | by_sector | funding_growth_qoq | 4Q | 45 | -0.0812 | n/a | 0.6043 | 0.9063 | Null: no evidence of an effect at this horizon |
| B-technology-1q | by_sector | funding_growth_qoq | 1Q | 48 | +0.2115 | n/a | 0.1528 | 0.9063 | Null: no evidence of an effect at this horizon |
| B-technology-2q | by_sector | funding_growth_qoq | 2Q | 47 | +0.0838 | n/a | 0.5679 | 0.9063 | Null: no evidence of an effect at this horizon |
| B-technology-4q | by_sector | funding_growth_qoq | 4Q | 45 | -0.1660 | n/a | 0.2745 | 0.9063 | Null: no evidence of an effect at this horizon |
| W01 | walk_forward | funding_growth_qoq | 1Q | 29 | +0.0226 | [-0.0061, +0.0537] | n/a | n/a | Sign agreement in 3/4 folds |
| W02 | walk_forward | funding_growth_qoq | 2Q | 28 | +0.0351 | [-0.0029, +0.0760] | n/a | n/a | Sign agreement in 4/4 folds |
| W03 | walk_forward | funding_growth_qoq | 4Q | 27 | +0.0328 | [-0.0301, +0.0884] | n/a | n/a | Sign agreement in 2/4 folds |

**48 hypothesis tests run; 0 survive Benjamini-Hochberg at q = 0.05 within their family.**

## Entries

### S01 - Cross-sectional tercile sort (top third minus bottom third), funding_growth_qoq, 1Q horizon

- **Protocol:** Each quarter rank sectors by funding_growth_qoq; long the top third, short the bottom third (k = n//3, min 6 sectors); hold 1Q. Statistic: mean quarterly spread (return). 95% CI: paired-by-quarter circular block bootstrap, block = 1 quarters (10,000 resamples, seed 0). Two-sided p: within-quarter permutation of returns (5,000 permutations).
- **Data:** PitchBook export; returns=raw, lag=0q; 2014Q2..2026Q1, 10 sectors, 469 sector-quarters
- **Result:** estimate +0.0127 (n = 48)
- **95% CI:** [-0.0063, +0.0324]
- **p-value:** 0.2418; BH-adjusted 0.4352
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Mean top-third return +0.0472, bottom-third +0.0345; hit rate (spread > 0) 58% of 48 quarters.

### S02 - Cross-sectional tercile sort (top third minus bottom third), funding_growth_qoq, 2Q horizon

- **Protocol:** Each quarter rank sectors by funding_growth_qoq; long the top third, short the bottom third (k = n//3, min 6 sectors); hold 2Q. Statistic: mean quarterly spread (return). 95% CI: paired-by-quarter circular block bootstrap, block = 2 quarters (10,000 resamples, seed 0). Two-sided p: within-quarter permutation of returns (5,000 permutations).
- **Data:** PitchBook export; returns=raw, lag=0q; 2014Q2..2025Q4, 10 sectors, 459 sector-quarters
- **Result:** estimate +0.0261 (n = 47)
- **95% CI:** [+0.0005, +0.0532]
- **p-value:** 0.0948; BH-adjusted 0.3971
- **Verdict:** Nominally significant but does NOT survive BH correction (or the CI and the permutation test disagree). No claim.
- Note: Mean top-third return +0.0930, bottom-third +0.0669; hit rate (spread > 0) 64% of 47 quarters.

### S03 - Cross-sectional tercile sort (top third minus bottom third), funding_growth_qoq, 4Q horizon

- **Protocol:** Each quarter rank sectors by funding_growth_qoq; long the top third, short the bottom third (k = n//3, min 6 sectors); hold 4Q. Statistic: mean quarterly spread (return). 95% CI: paired-by-quarter circular block bootstrap, block = 4 quarters (10,000 resamples, seed 0). Two-sided p: within-quarter permutation of returns (5,000 permutations).
- **Data:** PitchBook export; returns=raw, lag=0q; 2014Q2..2025Q2, 10 sectors, 439 sector-quarters
- **Result:** estimate +0.0233 (n = 45)
- **95% CI:** [-0.0196, +0.0650]
- **p-value:** 0.3315; BH-adjusted 0.4561
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Mean top-third return +0.1736, bottom-third +0.1503; hit rate (spread > 0) 53% of 45 quarters.

### S04 - Cross-sectional tercile sort (top third minus bottom third), deal_growth_qoq, 1Q horizon

- **Protocol:** Each quarter rank sectors by deal_growth_qoq; long the top third, short the bottom third (k = n//3, min 6 sectors); hold 1Q. Statistic: mean quarterly spread (return). 95% CI: paired-by-quarter circular block bootstrap, block = 1 quarters (10,000 resamples, seed 0). Two-sided p: within-quarter permutation of returns (5,000 permutations).
- **Data:** PitchBook export; returns=raw, lag=0q; 2014Q2..2026Q1, 10 sectors, 469 sector-quarters
- **Result:** estimate +0.0061 (n = 48)
- **95% CI:** [-0.0143, +0.0270]
- **p-value:** 0.5725; BH-adjusted 0.5725
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Mean top-third return +0.0455, bottom-third +0.0394; hit rate (spread > 0) 54% of 48 quarters.

### S05 - Cross-sectional tercile sort (top third minus bottom third), deal_growth_qoq, 2Q horizon

- **Protocol:** Each quarter rank sectors by deal_growth_qoq; long the top third, short the bottom third (k = n//3, min 6 sectors); hold 2Q. Statistic: mean quarterly spread (return). 95% CI: paired-by-quarter circular block bootstrap, block = 2 quarters (10,000 resamples, seed 0). Two-sided p: within-quarter permutation of returns (5,000 permutations).
- **Data:** PitchBook export; returns=raw, lag=0q; 2014Q2..2025Q4, 10 sectors, 459 sector-quarters
- **Result:** estimate +0.0234 (n = 47)
- **95% CI:** [-0.0078, +0.0547]
- **p-value:** 0.1324; BH-adjusted 0.3971
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Mean top-third return +0.0903, bottom-third +0.0669; hit rate (spread > 0) 60% of 47 quarters.

### S06 - Cross-sectional tercile sort (top third minus bottom third), deal_growth_qoq, 4Q horizon

- **Protocol:** Each quarter rank sectors by deal_growth_qoq; long the top third, short the bottom third (k = n//3, min 6 sectors); hold 4Q. Statistic: mean quarterly spread (return). 95% CI: paired-by-quarter circular block bootstrap, block = 4 quarters (10,000 resamples, seed 0). Two-sided p: within-quarter permutation of returns (5,000 permutations).
- **Data:** PitchBook export; returns=raw, lag=0q; 2014Q2..2025Q2, 10 sectors, 439 sector-quarters
- **Result:** estimate -0.0222 (n = 45)
- **95% CI:** [-0.0686, +0.0188]
- **p-value:** 0.3547; BH-adjusted 0.4561
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Mean top-third return +0.1524, bottom-third +0.1746; hit rate (spread > 0) 49% of 45 quarters.

### S07 - Cross-sectional tercile sort (top third minus bottom third), funding_growth_yoy, 1Q horizon

- **Protocol:** Each quarter rank sectors by funding_growth_yoy; long the top third, short the bottom third (k = n//3, min 6 sectors); hold 1Q. Statistic: mean quarterly spread (return). 95% CI: paired-by-quarter circular block bootstrap, block = 1 quarters (10,000 resamples, seed 0). Two-sided p: within-quarter permutation of returns (5,000 permutations).
- **Data:** PitchBook export; returns=raw, lag=0q; 2015Q1..2026Q1, 10 sectors, 444 sector-quarters
- **Result:** estimate +0.0186 (n = 45)
- **95% CI:** [-0.0035, +0.0430]
- **p-value:** 0.0894; BH-adjusted 0.3971
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Mean top-third return +0.0476, bottom-third +0.0289; hit rate (spread > 0) 56% of 45 quarters.

### S08 - Cross-sectional tercile sort (top third minus bottom third), funding_growth_yoy, 2Q horizon

- **Protocol:** Each quarter rank sectors by funding_growth_yoy; long the top third, short the bottom third (k = n//3, min 6 sectors); hold 2Q. Statistic: mean quarterly spread (return). 95% CI: paired-by-quarter circular block bootstrap, block = 2 quarters (10,000 resamples, seed 0). Two-sided p: within-quarter permutation of returns (5,000 permutations).
- **Data:** PitchBook export; returns=raw, lag=0q; 2015Q1..2025Q4, 10 sectors, 434 sector-quarters
- **Result:** estimate -0.0130 (n = 44)
- **95% CI:** [-0.0380, +0.0138]
- **p-value:** 0.4323; BH-adjusted 0.4864
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Mean top-third return +0.0678, bottom-third +0.0808; hit rate (spread > 0) 45% of 44 quarters.

### S09 - Cross-sectional tercile sort (top third minus bottom third), funding_growth_yoy, 4Q horizon

- **Protocol:** Each quarter rank sectors by funding_growth_yoy; long the top third, short the bottom third (k = n//3, min 6 sectors); hold 4Q. Statistic: mean quarterly spread (return). 95% CI: paired-by-quarter circular block bootstrap, block = 4 quarters (10,000 resamples, seed 0). Two-sided p: within-quarter permutation of returns (5,000 permutations).
- **Data:** PitchBook export; returns=raw, lag=0q; 2015Q1..2025Q2, 10 sectors, 414 sector-quarters
- **Result:** estimate -0.0330 (n = 42)
- **95% CI:** [-0.0783, +0.0121]
- **p-value:** 0.1856; BH-adjusted 0.4175
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Mean top-third return +0.1422, bottom-third +0.1752; hit rate (spread > 0) 38% of 42 quarters.

### P01 - Pooled Spearman rank correlation, funding_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho between funding_growth_qoq in quarter t and the 1Q forward return from the end of t (+lag), pooled over sector-quarters. 95% CI: percentile cluster bootstrap over quarters (10,000 resamples, seed 0). Two-sided p: permutation of returns within quarter (5,000 permutations).
- **Data:** PitchBook export; returns=raw, lag=0q; 2014Q2..2026Q1, 10 sectors, 469 sector-quarters
- **Result:** estimate +0.0712 (n = 469)
- **95% CI:** [-0.0491, +0.1872]
- **p-value:** 0.4129; BH-adjusted 0.5903
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: 48 quarter clusters.

### P02 - Pooled Spearman rank correlation, funding_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho between funding_growth_qoq in quarter t and the 2Q forward return from the end of t (+lag), pooled over sector-quarters. 95% CI: percentile cluster bootstrap over quarters (10,000 resamples, seed 0). Two-sided p: permutation of returns within quarter (5,000 permutations).
- **Data:** PitchBook export; returns=raw, lag=0q; 2014Q2..2025Q4, 10 sectors, 459 sector-quarters
- **Result:** estimate +0.0948 (n = 459)
- **95% CI:** [-0.0169, +0.2044]
- **p-value:** 0.0186; BH-adjusted 0.0837
- **Verdict:** Nominally significant but does NOT survive BH correction (or the CI and the permutation test disagree). No claim.
- Note: 47 quarter clusters.

### P03 - Pooled Spearman rank correlation, funding_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho between funding_growth_qoq in quarter t and the 4Q forward return from the end of t (+lag), pooled over sector-quarters. 95% CI: percentile cluster bootstrap over quarters (10,000 resamples, seed 0). Two-sided p: permutation of returns within quarter (5,000 permutations).
- **Data:** PitchBook export; returns=raw, lag=0q; 2014Q2..2025Q2, 10 sectors, 439 sector-quarters
- **Result:** estimate +0.0244 (n = 439)
- **95% CI:** [-0.1075, +0.1518]
- **p-value:** 0.4933; BH-adjusted 0.5903
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: 45 quarter clusters.

### P04 - Pooled Spearman rank correlation, deal_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho between deal_growth_qoq in quarter t and the 1Q forward return from the end of t (+lag), pooled over sector-quarters. 95% CI: percentile cluster bootstrap over quarters (10,000 resamples, seed 0). Two-sided p: permutation of returns within quarter (5,000 permutations).
- **Data:** PitchBook export; returns=raw, lag=0q; 2014Q2..2026Q1, 10 sectors, 469 sector-quarters
- **Result:** estimate +0.1106 (n = 469)
- **95% CI:** [-0.0398, +0.2580]
- **p-value:** 0.3815; BH-adjusted 0.5903
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: 48 quarter clusters.

### P05 - Pooled Spearman rank correlation, deal_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho between deal_growth_qoq in quarter t and the 2Q forward return from the end of t (+lag), pooled over sector-quarters. 95% CI: percentile cluster bootstrap over quarters (10,000 resamples, seed 0). Two-sided p: permutation of returns within quarter (5,000 permutations).
- **Data:** PitchBook export; returns=raw, lag=0q; 2014Q2..2025Q4, 10 sectors, 459 sector-quarters
- **Result:** estimate +0.0781 (n = 459)
- **95% CI:** [-0.0889, +0.2377]
- **p-value:** 0.0132; BH-adjusted 0.0837
- **Verdict:** Nominally significant but does NOT survive BH correction (or the CI and the permutation test disagree). No claim.
- Note: 47 quarter clusters.

### P06 - Pooled Spearman rank correlation, deal_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho between deal_growth_qoq in quarter t and the 4Q forward return from the end of t (+lag), pooled over sector-quarters. 95% CI: percentile cluster bootstrap over quarters (10,000 resamples, seed 0). Two-sided p: permutation of returns within quarter (5,000 permutations).
- **Data:** PitchBook export; returns=raw, lag=0q; 2014Q2..2025Q2, 10 sectors, 439 sector-quarters
- **Result:** estimate -0.0417 (n = 439)
- **95% CI:** [-0.2101, +0.1274]
- **p-value:** 0.5247; BH-adjusted 0.5903
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: 45 quarter clusters.

### P07 - Pooled Spearman rank correlation, funding_growth_yoy, 1Q horizon

- **Protocol:** Spearman rho between funding_growth_yoy in quarter t and the 1Q forward return from the end of t (+lag), pooled over sector-quarters. 95% CI: percentile cluster bootstrap over quarters (10,000 resamples, seed 0). Two-sided p: permutation of returns within quarter (5,000 permutations).
- **Data:** PitchBook export; returns=raw, lag=0q; 2015Q1..2026Q1, 10 sectors, 444 sector-quarters
- **Result:** estimate +0.0480 (n = 444)
- **95% CI:** [-0.0913, +0.1883]
- **p-value:** 0.0768; BH-adjusted 0.2304
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: 45 quarter clusters.

### P08 - Pooled Spearman rank correlation, funding_growth_yoy, 2Q horizon

- **Protocol:** Spearman rho between funding_growth_yoy in quarter t and the 2Q forward return from the end of t (+lag), pooled over sector-quarters. 95% CI: percentile cluster bootstrap over quarters (10,000 resamples, seed 0). Two-sided p: permutation of returns within quarter (5,000 permutations).
- **Data:** PitchBook export; returns=raw, lag=0q; 2015Q1..2025Q4, 10 sectors, 434 sector-quarters
- **Result:** estimate -0.0395 (n = 434)
- **95% CI:** [-0.1579, +0.0775]
- **p-value:** 0.6975; BH-adjusted 0.6975
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: 44 quarter clusters.

### P09 - Pooled Spearman rank correlation, funding_growth_yoy, 4Q horizon

- **Protocol:** Spearman rho between funding_growth_yoy in quarter t and the 4Q forward return from the end of t (+lag), pooled over sector-quarters. 95% CI: percentile cluster bootstrap over quarters (10,000 resamples, seed 0). Two-sided p: permutation of returns within quarter (5,000 permutations).
- **Data:** PitchBook export; returns=raw, lag=0q; 2015Q1..2025Q2, 10 sectors, 414 sector-quarters
- **Result:** estimate -0.1919 (n = 414)
- **95% CI:** [-0.3327, -0.0470]
- **p-value:** 0.1228; BH-adjusted 0.2762
- **Verdict:** Nominally significant but does NOT survive BH correction (or the CI and the permutation test disagree). No claim.
- Note: 42 quarter clusters.

### B-biotech-1q - Per-sector Spearman (biotech), funding_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 1Q forward return within sector 'biotech'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=raw, lag=0q; 2014Q2..2026Q1, 1 sectors, 48 sector-quarters
- **Result:** estimate -0.0337 (n = 48)
- **95% CI:** n/a
- **p-value:** 0.8156; BH-adjusted 0.9063
- **Verdict:** Null: no evidence of an effect at this horizon.

### B-biotech-2q - Per-sector Spearman (biotech), funding_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 2Q forward return within sector 'biotech'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=raw, lag=0q; 2014Q2..2025Q4, 1 sectors, 47 sector-quarters
- **Result:** estimate +0.2127 (n = 47)
- **95% CI:** n/a
- **p-value:** 0.1528; BH-adjusted 0.9063
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-biotech-4q - Per-sector Spearman (biotech), funding_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 4Q forward return within sector 'biotech'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=raw, lag=0q; 2014Q2..2025Q2, 1 sectors, 45 sector-quarters
- **Result:** estimate +0.0046 (n = 45)
- **95% CI:** n/a
- **p-value:** 0.9788; BH-adjusted 0.9810
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-cybersecurity-1q - Per-sector Spearman (cybersecurity), funding_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 1Q forward return within sector 'cybersecurity'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=raw, lag=0q; 2014Q4..2026Q1, 1 sectors, 46 sector-quarters
- **Result:** estimate +0.2127 (n = 46)
- **95% CI:** n/a
- **p-value:** 0.1470; BH-adjusted 0.9063
- **Verdict:** Null: no evidence of an effect at this horizon.

### B-cybersecurity-2q - Per-sector Spearman (cybersecurity), funding_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 2Q forward return within sector 'cybersecurity'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=raw, lag=0q; 2014Q4..2025Q4, 1 sectors, 45 sector-quarters
- **Result:** estimate +0.0381 (n = 45)
- **95% CI:** n/a
- **p-value:** 0.7922; BH-adjusted 0.9063
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-cybersecurity-4q - Per-sector Spearman (cybersecurity), funding_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 4Q forward return within sector 'cybersecurity'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=raw, lag=0q; 2014Q4..2025Q2, 1 sectors, 43 sector-quarters
- **Result:** estimate +0.0835 (n = 43)
- **95% CI:** n/a
- **p-value:** 0.6075; BH-adjusted 0.9063
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-energy-1q - Per-sector Spearman (energy), funding_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 1Q forward return within sector 'energy'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=raw, lag=0q; 2014Q2..2026Q1, 1 sectors, 48 sector-quarters
- **Result:** estimate +0.0629 (n = 48)
- **95% CI:** n/a
- **p-value:** 0.6667; BH-adjusted 0.9063
- **Verdict:** Null: no evidence of an effect at this horizon.

### B-energy-2q - Per-sector Spearman (energy), funding_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 2Q forward return within sector 'energy'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=raw, lag=0q; 2014Q2..2025Q4, 1 sectors, 47 sector-quarters
- **Result:** estimate +0.1294 (n = 47)
- **95% CI:** n/a
- **p-value:** 0.3799; BH-adjusted 0.9063
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-energy-4q - Per-sector Spearman (energy), funding_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 4Q forward return within sector 'energy'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=raw, lag=0q; 2014Q2..2025Q2, 1 sectors, 45 sector-quarters
- **Result:** estimate +0.0719 (n = 45)
- **95% CI:** n/a
- **p-value:** 0.6411; BH-adjusted 0.9063
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-financials-1q - Per-sector Spearman (financials), funding_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 1Q forward return within sector 'financials'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=raw, lag=0q; 2014Q2..2026Q1, 1 sectors, 48 sector-quarters
- **Result:** estimate +0.0689 (n = 48)
- **95% CI:** n/a
- **p-value:** 0.6457; BH-adjusted 0.9063
- **Verdict:** Null: no evidence of an effect at this horizon.

### B-financials-2q - Per-sector Spearman (financials), funding_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 2Q forward return within sector 'financials'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=raw, lag=0q; 2014Q2..2025Q4, 1 sectors, 47 sector-quarters
- **Result:** estimate +0.1285 (n = 47)
- **95% CI:** n/a
- **p-value:** 0.3833; BH-adjusted 0.9063
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-financials-4q - Per-sector Spearman (financials), funding_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 4Q forward return within sector 'financials'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=raw, lag=0q; 2014Q2..2025Q2, 1 sectors, 45 sector-quarters
- **Result:** estimate +0.2134 (n = 45)
- **95% CI:** n/a
- **p-value:** 0.1594; BH-adjusted 0.9063
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-fintech-1q - Per-sector Spearman (fintech), funding_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 1Q forward return within sector 'fintech'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=raw, lag=0q; 2016Q3..2026Q1, 1 sectors, 39 sector-quarters
- **Result:** estimate +0.0939 (n = 39)
- **95% CI:** n/a
- **p-value:** 0.5593; BH-adjusted 0.9063
- **Verdict:** Null: no evidence of an effect at this horizon.

### B-fintech-2q - Per-sector Spearman (fintech), funding_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 2Q forward return within sector 'fintech'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=raw, lag=0q; 2016Q3..2025Q4, 1 sectors, 38 sector-quarters
- **Result:** estimate -0.0524 (n = 38)
- **95% CI:** n/a
- **p-value:** 0.7419; BH-adjusted 0.9063
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-fintech-4q - Per-sector Spearman (fintech), funding_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 4Q forward return within sector 'fintech'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=raw, lag=0q; 2016Q3..2025Q2, 1 sectors, 36 sector-quarters
- **Result:** estimate -0.0571 (n = 36)
- **95% CI:** n/a
- **p-value:** 0.7435; BH-adjusted 0.9063
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-healthcare-1q - Per-sector Spearman (healthcare), funding_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 1Q forward return within sector 'healthcare'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=raw, lag=0q; 2014Q2..2026Q1, 1 sectors, 48 sector-quarters
- **Result:** estimate -0.0601 (n = 48)
- **95% CI:** n/a
- **p-value:** 0.6825; BH-adjusted 0.9063
- **Verdict:** Null: no evidence of an effect at this horizon.

### B-healthcare-2q - Per-sector Spearman (healthcare), funding_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 2Q forward return within sector 'healthcare'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=raw, lag=0q; 2014Q2..2025Q4, 1 sectors, 47 sector-quarters
- **Result:** estimate -0.0820 (n = 47)
- **95% CI:** n/a
- **p-value:** 0.5699; BH-adjusted 0.9063
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-healthcare-4q - Per-sector Spearman (healthcare), funding_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 4Q forward return within sector 'healthcare'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=raw, lag=0q; 2014Q2..2025Q2, 1 sectors, 45 sector-quarters
- **Result:** estimate +0.0399 (n = 45)
- **95% CI:** n/a
- **p-value:** 0.7924; BH-adjusted 0.9063
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-industrials-1q - Per-sector Spearman (industrials), funding_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 1Q forward return within sector 'industrials'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=raw, lag=0q; 2014Q2..2026Q1, 1 sectors, 48 sector-quarters
- **Result:** estimate -0.0144 (n = 48)
- **95% CI:** n/a
- **p-value:** 0.9230; BH-adjusted 0.9810
- **Verdict:** Null: no evidence of an effect at this horizon.

### B-industrials-2q - Per-sector Spearman (industrials), funding_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 2Q forward return within sector 'industrials'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=raw, lag=0q; 2014Q2..2025Q4, 1 sectors, 47 sector-quarters
- **Result:** estimate +0.0371 (n = 47)
- **95% CI:** n/a
- **p-value:** 0.8026; BH-adjusted 0.9063
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-industrials-4q - Per-sector Spearman (industrials), funding_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 4Q forward return within sector 'industrials'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=raw, lag=0q; 2014Q2..2025Q2, 1 sectors, 45 sector-quarters
- **Result:** estimate +0.0626 (n = 45)
- **95% CI:** n/a
- **p-value:** 0.6767; BH-adjusted 0.9063
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-semiconductors-1q - Per-sector Spearman (semiconductors), funding_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 1Q forward return within sector 'semiconductors'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=raw, lag=0q; 2014Q2..2026Q1, 1 sectors, 48 sector-quarters
- **Result:** estimate -0.0728 (n = 48)
- **95% CI:** n/a
- **p-value:** 0.6237; BH-adjusted 0.9063
- **Verdict:** Null: no evidence of an effect at this horizon.

### B-semiconductors-2q - Per-sector Spearman (semiconductors), funding_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 2Q forward return within sector 'semiconductors'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=raw, lag=0q; 2014Q2..2025Q4, 1 sectors, 47 sector-quarters
- **Result:** estimate +0.0537 (n = 47)
- **95% CI:** n/a
- **p-value:** 0.7283; BH-adjusted 0.9063
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-semiconductors-4q - Per-sector Spearman (semiconductors), funding_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 4Q forward return within sector 'semiconductors'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=raw, lag=0q; 2014Q2..2025Q2, 1 sectors, 45 sector-quarters
- **Result:** estimate +0.0038 (n = 45)
- **95% CI:** n/a
- **p-value:** 0.9810; BH-adjusted 0.9810
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-software-1q - Per-sector Spearman (software), funding_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 1Q forward return within sector 'software'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=raw, lag=0q; 2014Q2..2026Q1, 1 sectors, 48 sector-quarters
- **Result:** estimate +0.2670 (n = 48)
- **95% CI:** n/a
- **p-value:** 0.0666; BH-adjusted 0.9063
- **Verdict:** Null: no evidence of an effect at this horizon.

### B-software-2q - Per-sector Spearman (software), funding_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 2Q forward return within sector 'software'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=raw, lag=0q; 2014Q2..2025Q4, 1 sectors, 47 sector-quarters
- **Result:** estimate +0.1643 (n = 47)
- **95% CI:** n/a
- **p-value:** 0.2649; BH-adjusted 0.9063
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-software-4q - Per-sector Spearman (software), funding_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 4Q forward return within sector 'software'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=raw, lag=0q; 2014Q2..2025Q2, 1 sectors, 45 sector-quarters
- **Result:** estimate -0.0812 (n = 45)
- **95% CI:** n/a
- **p-value:** 0.6043; BH-adjusted 0.9063
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-technology-1q - Per-sector Spearman (technology), funding_growth_qoq, 1Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 1Q forward return within sector 'technology'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=raw, lag=0q; 2014Q2..2026Q1, 1 sectors, 48 sector-quarters
- **Result:** estimate +0.2115 (n = 48)
- **95% CI:** n/a
- **p-value:** 0.1528; BH-adjusted 0.9063
- **Verdict:** Null: no evidence of an effect at this horizon.

### B-technology-2q - Per-sector Spearman (technology), funding_growth_qoq, 2Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 2Q forward return within sector 'technology'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=raw, lag=0q; 2014Q2..2025Q4, 1 sectors, 47 sector-quarters
- **Result:** estimate +0.0838 (n = 47)
- **95% CI:** n/a
- **p-value:** 0.5679; BH-adjusted 0.9063
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### B-technology-4q - Per-sector Spearman (technology), funding_growth_qoq, 4Q horizon

- **Protocol:** Spearman rho over time between funding_growth_qoq and the 4Q forward return within sector 'technology'. Two-sided p: unrestricted permutation (5,000, seed 0); no CI reported (n small; the BH-adjusted p is the decision statistic).
- **Data:** PitchBook export; returns=raw, lag=0q; 2014Q2..2025Q2, 1 sectors, 45 sector-quarters
- **Result:** estimate -0.1660 (n = 45)
- **95% CI:** n/a
- **p-value:** 0.2745; BH-adjusted 0.9063
- **Verdict:** Null: no evidence of an effect at this horizon.
- Note: Time-permutation p ignores overlap at h>1: anti-conservative.

### W01 - Walk-forward sign persistence of the tercile spread, funding_growth_qoq, 1Q horizon

- **Protocol:** Expanding-window walk-forward with 4 test folds over the quarterly spread series from S01; first 40% of quarters is the initial training window. Report per-fold train/test mean spread and sign agreement, plus the pooled OOS mean with a block bootstrap CI (block = 1, 10,000 resamples, seed 0).
- **Data:** PitchBook export; returns=raw, lag=0q; 2014Q2..2026Q1, 10 sectors, 469 sector-quarters
- **Result:** estimate +0.0226 (n = 29)
- **95% CI:** [-0.0061, +0.0537]
- **p-value:** n/a
- **Verdict:** Sign agreement in 3/4 folds. OOS CI includes 0. Descriptive: no hypothesis test entered into BH.
- Note: Fold 1: train to 2018Q4 mean -0.0025; test 2019Q1..2020Q3 (n=7) mean +0.0191; DISAGREE
- Note: Fold 2: train to 2020Q3 mean +0.0033; test 2020Q4..2022Q3 (n=8) mean +0.0226; agree
- Note: Fold 3: train to 2022Q3 mean +0.0079; test 2022Q4..2024Q2 (n=7) mean +0.0201; agree
- Note: Fold 4: train to 2024Q2 mean +0.0100; test 2024Q3..2026Q1 (n=7) mean +0.0287; agree

### W02 - Walk-forward sign persistence of the tercile spread, funding_growth_qoq, 2Q horizon

- **Protocol:** Expanding-window walk-forward with 4 test folds over the quarterly spread series from S02; first 40% of quarters is the initial training window. Report per-fold train/test mean spread and sign agreement, plus the pooled OOS mean with a block bootstrap CI (block = 2, 10,000 resamples, seed 0).
- **Data:** PitchBook export; returns=raw, lag=0q; 2014Q2..2025Q4, 10 sectors, 459 sector-quarters
- **Result:** estimate +0.0351 (n = 28)
- **95% CI:** [-0.0029, +0.0760]
- **p-value:** n/a
- **Verdict:** Sign agreement in 4/4 folds. OOS CI includes 0. Descriptive: no hypothesis test entered into BH.
- Note: Fold 1: train to 2018Q4 mean +0.0127; test 2019Q1..2020Q3 (n=7) mean +0.0302; agree
- Note: Fold 2: train to 2020Q3 mean +0.0174; test 2020Q4..2022Q2 (n=7) mean +0.0635; agree
- Note: Fold 3: train to 2022Q2 mean +0.0272; test 2022Q3..2024Q1 (n=7) mean +0.0185; agree
- Note: Fold 4: train to 2024Q1 mean +0.0257; test 2024Q2..2025Q4 (n=7) mean +0.0283; agree

### W03 - Walk-forward sign persistence of the tercile spread, funding_growth_qoq, 4Q horizon

- **Protocol:** Expanding-window walk-forward with 4 test folds over the quarterly spread series from S03; first 40% of quarters is the initial training window. Report per-fold train/test mean spread and sign agreement, plus the pooled OOS mean with a block bootstrap CI (block = 4, 10,000 resamples, seed 0).
- **Data:** PitchBook export; returns=raw, lag=0q; 2014Q2..2025Q2, 10 sectors, 439 sector-quarters
- **Result:** estimate +0.0328 (n = 27)
- **95% CI:** [-0.0301, +0.0884]
- **p-value:** n/a
- **Verdict:** Sign agreement in 2/4 folds. OOS CI includes 0. Descriptive: no hypothesis test entered into BH.
- Note: Fold 1: train to 2018Q3 mean +0.0091; test 2018Q4..2020Q2 (n=7) mean -0.0720; DISAGREE
- Note: Fold 2: train to 2020Q2 mean -0.0136; test 2020Q3..2022Q1 (n=7) mean +0.0773; DISAGREE
- Note: Fold 3: train to 2022Q1 mean +0.0063; test 2022Q2..2023Q3 (n=6) mean +0.0710; agree
- Note: Fold 4: train to 2023Q3 mean +0.0165; test 2023Q4..2025Q2 (n=7) mean +0.0604; agree
