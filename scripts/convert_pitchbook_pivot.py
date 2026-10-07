"""Convert PitchBook "Deal Pivot Table" exports (xlsx, or the same grid as CSV) into data/pitchbook_export.csv.

Expected pivot layout (one file per column dimension):
  rows    = Year > Quarter
  columns = a PitchBook industry dimension (Primary Sector / Group / Code / Verticals)
  values  = Deal Count, Capital Invested (sum, $M), Capital Invested Count,
            Post Valuation Median ($M)

Usage:
  python scripts/convert_pitchbook_pivot.py data/raw/*.xlsx

Which raw column feeds which study sector is defined in SECTOR_SOURCES below.
The raw exports stay in data/raw/ (git-ignored); only the derived sector x
quarter CSV is written, and it is git-ignored too.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "pitchbook_export.csv"

# study sector -> (pivot dimension header, raw column label as PitchBook prints it)
SECTOR_SOURCES = {
    "technology": ("Primary PitchBook Industry Sector", "Information Technology"),
    "healthcare": ("Primary PitchBook Industry Sector", "Healthcare"),
    "financials": ("Primary PitchBook Industry Sector", "Financial Services"),
    "energy": ("Primary PitchBook Industry Sector", "Energy"),
    "industrials": ("Primary PitchBook Industry Sector", "(B2B)"),
    "software": ("Primary PitchBook Industry Group", "Software"),
    "semiconductors": ("Primary PitchBook Industry Group", "Semiconductors"),
    "biotech": ("Primary PitchBook Industry Code", "Biotechnology"),
    "cybersecurity": ("Verticals", "Cybersecurity"),
    "fintech": ("Verticals", "FinTech"),
}
VALUE_COLS = ["Deal Count", "Capital Invested", "Capital Invested Count", "Post Valuation Median"]


def parse_pivot(path: Path) -> tuple[str, pd.DataFrame]:
    """Return (dimension_name, long DataFrame[raw_label, quarter, <values>])."""
    if path.suffix.lower() == ".csv":   # same grid, saved as CSV (e.g. parsed in-browser)
        raw = pd.read_csv(path, header=None)
    else:
        raw = pd.read_excel(path, sheet_name="Pivot Table", header=None)
    # locate the dimension header row: the cell in column 2 naming the column field
    dim_row = next(i for i in range(len(raw)) if isinstance(raw.iat[i, 2], str)
                   and raw.iat[i, 2].startswith(("Primary PitchBook", "Verticals", "GECS", "NAICS", "SIC")))
    dim = raw.iat[dim_row, 2].strip()
    header = raw.iloc[dim_row + 1]
    labels = raw.iloc[dim_row].ffill()
    first_data = dim_row + 3  # dim row, value-header row, "Year/Quarter" row
    body = raw.iloc[first_data:].copy()
    body[1] = body[1].ffill()
    body = body[body[2].astype(str).str.fullmatch(r"[1-4]Q") & body[1].astype(str).str.fullmatch(r"\d{4}")]
    quarters = [pd.Period(f"{int(y)}Q{q[0]}", freq="Q") for y, q in zip(body[1], body[2])]

    pieces = []
    for col in range(4, raw.shape[1]):
        label, val = labels.iat[col], header.iat[col]
        if not isinstance(val, str) or val not in VALUE_COLS or not isinstance(label, str):
            continue
        if label.strip() == "All":
            continue
        s = pd.to_numeric(body[col].replace({"-": np.nan, "—": np.nan}), errors="coerce")
        pieces.append(pd.DataFrame({"raw_label": label.strip(), "quarter": quarters, "value": s.to_numpy(), "field": val}))
    long = pd.concat(pieces).pivot_table(index=["raw_label", "quarter"], columns="field", values="value", aggfunc="first").reset_index()
    long.columns.name = None
    return dim, long


def main(paths: list[str]) -> None:
    tables: dict[str, pd.DataFrame] = {}
    for p in paths:
        dim, long = parse_pivot(Path(p))
        print(f"[convert] {Path(p).name}: dimension={dim!r}, {long['raw_label'].nunique()} labels, "
              f"{long['quarter'].min()}..{long['quarter'].max()}")
        tables[dim] = pd.concat([tables.get(dim, pd.DataFrame()), long])

    rows = []
    for sector, (dim, label) in SECTOR_SOURCES.items():
        if dim not in tables:
            print(f"[convert] WARNING: no export for dimension {dim!r}; sector {sector} skipped")
            continue
        t = tables[dim]
        sub = t[t["raw_label"] == label]
        if sub.empty:
            print(f"[convert] WARNING: label {label!r} not found in {dim!r} export "
                  f"(have: {sorted(t['raw_label'].unique())[:12]}...); sector {sector} skipped")
            continue
        for r in sub.to_dict("records"):
            rows.append({
                "sector": sector,
                "quarter": str(r["quarter"]),
                # PitchBook reports capital and valuations in $ millions
                "total_funding_usd": float(r.get("Capital Invested", np.nan)) * 1e6,
                "deal_count": int(r["Deal Count"]),
                "median_valuation_usd": float(r.get("Post Valuation Median", np.nan)) * 1e6,
                "deals_with_size": r.get("Capital Invested Count", np.nan),
                "source_dimension": dim,
                "source_label": label,
            })
    out = pd.DataFrame(rows).sort_values(["sector", "quarter"])
    OUT.write_text("# PitchBook-derived sector x quarter table. LICENSED DATA: do not commit or redistribute. "
                   "Built by scripts/convert_pitchbook_pivot.py from data/raw/*.xlsx\n")
    out.to_csv(OUT, mode="a", index=False)
    print(f"[convert] wrote {OUT} ({len(out)} rows, {out['sector'].nunique()} sectors)")


if __name__ == "__main__":
    main(sys.argv[1:] or [str(p) for p in sorted((ROOT / "data" / "raw").glob("*"))
                          if p.suffix.lower() in (".xlsx", ".csv")])
