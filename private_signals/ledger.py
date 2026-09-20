"""Render the experiment ledger (ledger.md) from a list of Experiment records."""
from __future__ import annotations

import subprocess
from datetime import date

import numpy as np
import pandas as pd

from .experiments import Experiment


def _fmt(x, nd=4) -> str:
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return "n/a"
    return f"{x:+.{nd}f}"


def _fmt_p(p) -> str:
    if p is None or (isinstance(p, float) and np.isnan(p)):
        return "n/a"
    return f"{p:.4f}" if p >= 1e-4 else f"{p:.1e}"


def _git_sha() -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], text=True).strip()
    except Exception:
        return "unknown"


def summary_table(exps: list[Experiment]) -> pd.DataFrame:
    return pd.DataFrame([{
        "id": e.id, "family": e.family, "feature": e.feature, "horizon_q": e.horizon,
        "n": e.n, "estimate": e.estimate, "ci_low": e.ci_low, "ci_high": e.ci_high,
        "p": e.pvalue, "p_bh": e.p_adj, "verdict": e.verdict,
    } for e in exps])


def render_ledger(exps: list[Experiment], meta: dict) -> str:
    synthetic = meta.get("synthetic", False)
    lines = ["# Experiment ledger", ""]
    if synthetic:
        lines += [
            "> **WARNING: EVERY NUMBER BELOW WAS COMPUTED ON THE SYNTHETIC FIXTURE (FAKE DATA).**",
            "> The private-funding side is a seeded random process with no relationship to real",
            "> markets. This ledger exists to show the pipeline runs end to end. Nothing in it is a",
            "> finding. Re-run with a PitchBook export (see `data/README.md`) to get real entries.",
            "",
        ]
    lines += [
        f"Generated {date.today().isoformat()} at commit `{_git_sha()}` by `scripts/run_experiments.py`.",
        "",
        "## Run configuration", "",
        "| setting | value |", "|---|---|",
    ]
    for k, v in meta.items():
        lines.append(f"| {k} | {v} |")
    lines += ["", "## Summary", ""]
    lines += ["| id | family | feature | h | n | estimate | 95% CI | p | BH p | verdict |",
              "|---|---|---|---|---|---|---|---|---|---|"]
    for e in exps:
        ci = "n/a" if np.isnan(e.ci_low) else f"[{_fmt(e.ci_low)}, {_fmt(e.ci_high)}]"
        short = e.verdict.split(".")[0]
        lines.append(f"| {e.id} | {e.family} | {e.feature} | {e.horizon}Q | {e.n} | {_fmt(e.estimate)} | {ci} | "
                     f"{_fmt_p(e.pvalue)} | {_fmt_p(e.p_adj)} | {short} |")
    n_tests = sum(e.pvalue is not None for e in exps)
    n_surv = sum((e.p_adj is not None and e.p_adj <= 0.05 and e.ci_excludes_zero) for e in exps)
    lines += ["", f"**{n_tests} hypothesis tests run; {n_surv} survive Benjamini-Hochberg at q = 0.05 "
                  "within their family.**", ""]
    lines += ["## Entries", ""]
    for e in exps:
        lines += [f"### {e.id} - {e.name}, {e.feature}, {e.horizon}Q horizon", "",
                  f"- **Protocol:** {e.protocol}",
                  f"- **Data:** {e.data}",
                  f"- **Result:** estimate {_fmt(e.estimate)} (n = {e.n})",
                  f"- **95% CI:** " + ("n/a" if np.isnan(e.ci_low) else f"[{_fmt(e.ci_low)}, {_fmt(e.ci_high)}]"),
                  f"- **p-value:** {_fmt_p(e.pvalue)}" + (f"; BH-adjusted {_fmt_p(e.p_adj)}" if e.p_adj is not None else ""),
                  f"- **Verdict:** {e.verdict}"]
        for n in e.notes:
            lines.append(f"- Note: {n}")
        lines.append("")
    return "\n".join(lines)
