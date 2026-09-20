"""Matplotlib figures. Conventions: one hue per job, thin marks, recessive
axes, direct labels, and a loud SYNTHETIC watermark when the data is fake."""
from __future__ import annotations

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.colors import LinearSegmentedColormap  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from .experiments import Experiment  # noqa: E402

BLUE, ORANGE, AQUA = "#2a78d6", "#eb6834", "#1baf7a"
INK, INK2, GRID, SURFACE = "#0b0b0b", "#52514e", "#e6e5e1", "#fcfcfb"
DIVERGING = LinearSegmentedColormap.from_list("ps_div", [BLUE, "#d9d8d3", ORANGE])

plt.rcParams.update({
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "savefig.facecolor": SURFACE,
    "axes.edgecolor": GRID, "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.8,
    "axes.labelcolor": INK2, "xtick.color": INK2, "ytick.color": INK2, "text.color": INK,
    "font.size": 10, "axes.titlesize": 11, "axes.titleweight": "bold", "axes.titlelocation": "left",
})


def _watermark(fig, synthetic: bool) -> None:
    if synthetic:
        fig.text(0.5, 0.5, "SYNTHETIC DATA", fontsize=48, color=ORANGE, alpha=0.18,
                 ha="center", va="center", rotation=25, weight="bold", zorder=0)


def _save(fig, out_dir: Path, name: str) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / name
    fig.savefig(path, dpi=160, bbox_inches="tight")
    plt.close(fig)
    return path


def plot_sort_spreads(sorts: list[Experiment], out_dir: Path, synthetic: bool, unit: str) -> Path:
    """Point estimate + 95% CI of the tercile spread, one panel per feature, horizons on x."""
    feats = list(dict.fromkeys(e.feature for e in sorts))
    fig, axes = plt.subplots(1, len(feats), figsize=(3.4 * len(feats), 3.9), sharey=True, layout="constrained")
    axes = np.atleast_1d(axes)
    for ax, f in zip(axes, feats):
        es = sorted([e for e in sorts if e.feature == f], key=lambda e: e.horizon)
        x = np.arange(len(es))
        for xi, e in zip(x, es):
            survives = e.p_adj is not None and e.p_adj <= 0.05 and e.ci_excludes_zero
            ax.plot([xi, xi], [e.ci_low, e.ci_high], color=BLUE, lw=2, solid_capstyle="round")
            ax.plot(xi, e.estimate, "o", ms=8, color=BLUE, mec=SURFACE, mew=2)
            ax.annotate(f"{e.estimate:+.3f}\np={e.pvalue:.2f}", (xi, e.ci_high), textcoords="offset points",
                        xytext=(0, 6), ha="center", fontsize=8, color=INK2)
            if survives:
                ax.plot(xi, e.estimate, "o", ms=14, mfc="none", mec=ORANGE, mew=1.5)
        ax.axhline(0, color=INK2, lw=0.8)
        ax.margins(y=0.25)
        ax.set_xticks(x, [f"{e.horizon}Q" for e in es])
        ax.set_title(f)
        ax.grid(axis="x", visible=False)
    axes[0].set_ylabel(f"top-third minus bottom-third forward {unit}")
    fig.suptitle("Cross-sectional sorts: mean top-third minus bottom-third spread, 95% block-bootstrap CI",
                 ha="left", x=0.02, fontsize=11, weight="bold")
    fig.supxlabel("Orange ring = survives Benjamini-Hochberg (q=0.05) within the sort family.",
                  ha="left", x=0.02, fontsize=8, color=INK2)
    _watermark(fig, synthetic)
    return _save(fig, out_dir, "sort_spreads.png")


def plot_cumulative_spread(sort_exp: Experiment, wf_exp: Experiment, out_dir: Path,
                           synthetic: bool, unit: str) -> Path:
    """Cumulative quarterly tercile spread with walk-forward test folds shaded."""
    sp = sort_exp.extra["spreads"]["spread"]
    cum = sp.cumsum()
    x = cum.index.to_timestamp(how="end")
    fig, ax = plt.subplots(figsize=(8, 3.8), layout="constrained")
    folds = wf_exp.extra["folds"]
    for r in folds.itertuples():
        a = pd.Period(r.test_start, freq="Q").to_timestamp(how="start")
        b = pd.Period(r.test_end, freq="Q").to_timestamp(how="end")
        ax.axvspan(a, b, color=AQUA if r.agrees else ORANGE, alpha=0.12, lw=0)
    ax.plot(x, cum.values, color=BLUE, lw=2)
    ax.plot(x[-1], cum.values[-1], "o", color=BLUE, ms=6)
    ax.annotate(f"{cum.values[-1]:+.2f}", (x[-1], cum.values[-1]), textcoords="offset points",
                xytext=(6, 0), va="center", fontsize=9)
    ax.axhline(0, color=INK2, lw=0.8)
    ax.set_title(f"Cumulative {sort_exp.horizon}Q tercile spread, {sort_exp.feature}")
    ax.set_ylabel(f"cumulative spread ({unit})")
    fig.supxlabel("Shaded = walk-forward test folds: green agrees with the in-sample sign, orange disagrees.",
                  ha="left", x=0.02, fontsize=8, color=INK2)
    ax.grid(axis="x", visible=False)
    _watermark(fig, synthetic)
    return _save(fig, out_dir, f"cumulative_spread_{sort_exp.horizon}q.png")


def plot_sector_heatmap(by_sector: list[Experiment], out_dir: Path, synthetic: bool) -> Path:
    """Sectors x horizons heatmap of Spearman rho; cells surviving BH are ringed."""
    df = pd.DataFrame([{"sector": e.id.split("-")[1], "h": e.horizon, "rho": e.estimate,
                        "sig": e.p_adj is not None and e.p_adj <= 0.05} for e in by_sector])
    mat = df.pivot(index="sector", columns="h", values="rho").sort_index()
    sig = df.pivot(index="sector", columns="h", values="sig").sort_index()
    fig, ax = plt.subplots(figsize=(4.8, 0.42 * len(mat) + 1.4), layout="constrained")
    im = ax.imshow(mat.values, cmap=DIVERGING, vmin=-0.6, vmax=0.6, aspect="auto")
    ax.set_xticks(range(mat.shape[1]), [f"{h}Q" for h in mat.columns])
    ax.set_yticks(range(mat.shape[0]), mat.index)
    ax.grid(False)
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            v = mat.values[i, j]
            ax.text(j, i, f"{v:+.2f}", ha="center", va="center", fontsize=8,
                    color=SURFACE if abs(v) > 0.35 else INK)
            if sig.values[i, j]:
                ax.add_patch(plt.Rectangle((j - 0.5, i - 0.5), 1, 1, fill=False, ec=INK, lw=2))
    cb = fig.colorbar(im, ax=ax, fraction=0.05, pad=0.03)
    cb.set_label("Spearman rho", color=INK2)
    cb.outline.set_visible(False)
    ax.set_title(f"Per-sector rank correlation, {by_sector[0].feature}\n(black frame = survives BH, q=0.05)")
    _watermark(fig, synthetic)
    return _save(fig, out_dir, "sector_rank_corr_heatmap.png")


def plot_bh(exps: list[Experiment], out_dir: Path, synthetic: bool, q: float = 0.05) -> Path:
    """Sorted p-values against the BH step-up line, one panel per family."""
    fams = [f for f in ("sorts", "pooled", "by_sector") if any(e.family == f for e in exps)]
    fig, axes = plt.subplots(1, len(fams), figsize=(3.4 * len(fams), 3.6), layout="constrained")
    axes = np.atleast_1d(axes)
    for ax, fam in zip(axes, fams):
        p = np.sort([e.pvalue for e in exps if e.family == fam and e.pvalue is not None])
        m = len(p)
        k = np.arange(1, m + 1)
        ax.plot(k, q * k / m, color=ORANGE, lw=1.5, label=f"BH threshold q·k/m (q={q})")
        ax.plot(k, p, "o", color=BLUE, ms=6, mec=SURFACE, mew=1, label="sorted p-values")
        ax.set_ylim(0, 1.02)
        ax.set_title(f"{fam} (m={m})")
        ax.set_xlabel("rank k")
        ax.grid(axis="x", visible=False)
    axes[0].set_ylabel("p-value")
    axes[0].legend(frameon=False, fontsize=8, loc="upper left")
    fig.suptitle("Multiple testing: a hypothesis survives only where its dot falls below the BH line",
                 ha="left", x=0.02, fontsize=11, weight="bold")
    _watermark(fig, synthetic)
    return _save(fig, out_dir, "bh_pvalues.png")
