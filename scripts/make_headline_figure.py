"""figures/headline.png: the one chart that tells the story.

Left: cumulative 2Q tercile spread with the signal assumed known at quarter
end (lag 0) versus lagged one quarter for reporting delay (lag 1).
Right: the 2Q sort spread with 95% CI across the return-mode / lag variants
(read from the committed summary tables, so this never recomputes statistics).
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from private_signals.experiments import PRIMARY_FEATURE, tercile_spreads  # noqa: E402
from private_signals.figures import BLUE, GRID, INK, INK2, ORANGE, SURFACE, _save, _watermark  # noqa: E402
from private_signals.loader import load_prices, load_private  # noqa: E402
from private_signals.panel import build_panel  # noqa: E402
from private_signals.sectors import MARKET_ETF, SECTOR_MAP  # noqa: E402

H = 2
VARIANTS = [  # (label, summary.csv path)
    ("beta-neutral,\nlag 0 (primary)", ROOT / "results" / "summary.csv"),
    ("raw returns,\nlag 0", ROOT / "results" / "robustness" / "raw_lag0" / "results" / "summary.csv"),
    ("beta-neutral,\nlag 1 (reporting delay)", ROOT / "results" / "robustness" / "excess_lag1" / "results" / "summary.csv"),
]


def main() -> None:
    private = load_private()
    synthetic = bool(private.attrs.get("synthetic"))
    prices = load_prices(list(SECTOR_MAP.values()) + [MARKET_ETF])
    cum = {}
    for lag in (0, 1):
        panel = build_panel(private, prices, mode="excess", lag=lag)
        sp = tercile_spreads(panel, PRIMARY_FEATURE, H)["spread"]
        cum[lag] = sp.cumsum()

    fig, (ax, bx) = plt.subplots(1, 2, figsize=(11, 4.2), width_ratios=[1.6, 1], layout="constrained")

    # --- left: cumulative spread, lag 0 vs lag 1 ---
    ax.axvspan(pd.Timestamp("2020-07-01"), pd.Timestamp("2022-12-31"), color=GRID, alpha=0.6, lw=0)
    ax.text(pd.Timestamp("2021-09-01"), ax.get_ylim()[1] if False else 1.08, "2021 boom / 2022 bust",
            ha="center", va="bottom", fontsize=8, color=INK2)
    for lag, color, label in ((0, BLUE, "signal known at quarter end (lag 0)"),
                              (1, ORANGE, "signal lagged one quarter (lag 1)")):
        s = cum[lag]
        x = s.index.to_timestamp(how="end")
        ax.plot(x, s.values, color=color, lw=2)
        ax.annotate(f"{label}\n{s.values[-1]:+.2f}", (x[-1], s.values[-1]), textcoords="offset points",
                    xytext=(6, 0), va="center", fontsize=8.5, color=color)
    ax.axhline(0, color=INK2, lw=0.8)
    ax.set_xlim(right=pd.Timestamp("2028-09-30"))
    ax.set_ylim(-0.3, 1.25)
    ax.set_title("Cumulative 2Q top-third minus bottom-third spread, funding growth")
    ax.set_ylabel("cumulative excess return")
    ax.grid(axis="x", visible=False)

    # --- right: 2Q sort spread with CI across variants ---
    rows = []
    for label, path in VARIANTS:
        df = pd.read_csv(path)
        r = df[(df["id"] == "S02")].iloc[0]
        rows.append((label, r["estimate"], r["ci_low"], r["ci_high"], r["p"]))
    for i, (label, est, lo, hi, p) in enumerate(rows):
        color = ORANGE if "lag 1" in label else BLUE
        bx.plot([lo, hi], [i, i], color=color, lw=2, solid_capstyle="round")
        bx.plot(est, i, "o", ms=8, color=color, mec=SURFACE, mew=2)
        bx.annotate(f"{est:+.1%}  p={p:.2f}", (hi, i), textcoords="offset points", xytext=(6, 0),
                    va="center", fontsize=8.5, color=INK2)
    bx.axvline(0, color=INK2, lw=0.8)
    bx.set_yticks(range(len(rows)), [r[0] for r in rows], fontsize=8.5)
    bx.invert_yaxis()
    bx.set_xlim(-0.03, 0.09)
    bx.xaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1.0, decimals=0))
    bx.set_title("2Q spread per half-year, 95% block-bootstrap CI")
    bx.grid(axis="y", visible=False)

    fig.suptitle("The 2-quarter funding signal exists only if funding is assumed known the day the quarter ends",
                 ha="left", x=0.02, fontsize=11.5, weight="bold")
    fig.supxlabel("None of the 48 pre-specified tests survives Benjamini-Hochberg at q = 0.05. "
                  "Shaded band: the one regime that generates the lag-0 spread.",
                  ha="left", x=0.02, fontsize=8.5, color=INK2)
    _watermark(fig, synthetic)
    out = _save(fig, ROOT / "figures", "headline.png")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
