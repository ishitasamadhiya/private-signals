"""Run every experiment, write ledger.md, results/, and figures/.

    .venv/bin/python scripts/run_experiments.py                 # uses data/pitchbook_export.csv or the fixture
    .venv/bin/python scripts/run_experiments.py --mode raw --lag 1
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from private_signals.experiments import (  # noqa: E402
    PRIMARY_FEATURE, assign_verdicts, cross_sectional_sort, per_sector_rank_correlation,
    pooled_rank_correlation, walk_forward_sort,
)
from private_signals.figures import (  # noqa: E402
    plot_bh, plot_cumulative_spread, plot_sector_heatmap, plot_sort_spreads,
)
from private_signals.ledger import render_ledger, summary_table  # noqa: E402
from private_signals.loader import load_prices, load_private  # noqa: E402
from private_signals.panel import FEATURES, HORIZONS, build_panel  # noqa: E402
from private_signals.sectors import MARKET_ETF, SECTOR_MAP  # noqa: E402


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--private", default=None, help="PitchBook CSV; defaults to data/pitchbook_export.csv or the synthetic fixture")
    ap.add_argument("--mode", default="excess", choices=["raw", "excess", "vol_adj"])
    ap.add_argument("--lag", type=int, default=0)
    ap.add_argument("--start", default="2014-01-01")
    ap.add_argument("--n-boot", type=int, default=10_000)
    ap.add_argument("--n-perm", type=int, default=5_000)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--refresh-prices", action="store_true")
    ap.add_argument("--out", default=str(ROOT))
    args = ap.parse_args()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    private = load_private(args.private)
    prices = load_prices(list(SECTOR_MAP.values()) + [MARKET_ETF], start=args.start, refresh=args.refresh_prices)
    panel = build_panel(private, prices, mode=args.mode, lag=args.lag)
    synthetic = bool(panel.attrs.get("synthetic"))
    unit = "excess return" if args.mode == "excess" else ("return in sigmas" if args.mode == "vol_adj" else "return")
    print(f"[run] private source: {private.attrs['source']}  synthetic={synthetic}")
    print(f"[run] panel: {panel.shape[0]} rows, {panel['quarter'].min()}..{panel['quarter'].max()}, mode={args.mode}, lag={args.lag}")

    exps = []
    i = 0
    for f in FEATURES:
        for h in HORIZONS:
            i += 1
            exps.append(cross_sectional_sort(panel, f, h, f"S{i:02d}", args.n_boot, args.n_perm, args.seed))
            print(f"[run] {exps[-1].id} {f} {h}Q spread={exps[-1].estimate:+.4f} p={exps[-1].pvalue:.3f}")
    sorts = list(exps)
    i = 0
    for f in FEATURES:
        for h in HORIZONS:
            i += 1
            exps.append(pooled_rank_correlation(panel, f, h, f"P{i:02d}", args.n_boot, args.n_perm, args.seed))
            print(f"[run] {exps[-1].id} {f} {h}Q rho={exps[-1].estimate:+.4f} p={exps[-1].pvalue:.3f}")
    by_sector = per_sector_rank_correlation(panel, PRIMARY_FEATURE, HORIZONS, "B", args.n_perm, args.seed)
    exps += by_sector
    print(f"[run] {len(by_sector)} per-sector tests")
    wfs = []
    for k, s in enumerate([e for e in sorts if e.feature == PRIMARY_FEATURE], 1):
        wfs.append(walk_forward_sort(s, f"W{k:02d}", n_boot=args.n_boot, seed=args.seed))
    exps += wfs
    assign_verdicts(exps)

    meta = {
        "synthetic": synthetic, "private_source": Path(private.attrs["source"]).name,
        "return_mode": args.mode, "signal_lag_quarters": args.lag, "horizons_q": list(HORIZONS),
        "features": list(FEATURES), "primary_feature": PRIMARY_FEATURE,
        "sectors": ", ".join(f"{k}->{v}" for k, v in SECTOR_MAP.items()), "market": MARKET_ETF,
        "price_sample": f"{prices.index.min().date()}..{prices.index.max().date()}",
        "panel_quarters": f"{panel['quarter'].min()}..{panel['quarter'].max()}",
        "n_boot": args.n_boot, "n_perm": args.n_perm, "seed": args.seed, "bh_q": 0.05,
    }
    (out / "ledger.md").write_text(render_ledger(exps, meta))
    res = out / "results"
    res.mkdir(exist_ok=True)
    summary_table(exps).to_csv(res / "summary.csv", index=False)
    (res / "run_meta.json").write_text(json.dumps(meta, indent=2, default=str))
    panel.to_csv(res / "panel.csv", index=False)

    figs = out / "figures"
    plot_sort_spreads(sorts, figs, synthetic, unit)
    primary_sorts = {e.horizon: e for e in sorts if e.feature == PRIMARY_FEATURE}
    for w in wfs:
        plot_cumulative_spread(primary_sorts[w.horizon], w, figs, synthetic, unit)
    plot_sector_heatmap(by_sector, figs, synthetic)
    plot_bh(exps, figs, synthetic)
    n_tests = sum(e.pvalue is not None for e in exps)
    n_surv = sum((e.p_adj is not None and e.p_adj <= 0.05 and e.ci_excludes_zero) for e in exps)
    print(f"[run] wrote ledger.md, results/, figures/. {n_tests} tests, {n_surv} survive BH.")


if __name__ == "__main__":
    main()
