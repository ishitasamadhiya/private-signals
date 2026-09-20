"""Loaders for the two data sides.

Private side: a PitchBook sector x quarter export supplied by the user, or the
committed synthetic fixture (FAKE DATA) when no export is present.

Public side: daily adjusted closes from Yahoo Finance via yfinance, cached to
disk so repeated runs do not hit the network.
"""
from __future__ import annotations

import re
import warnings
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
CACHE_DIR = ROOT / "cache"
DEFAULT_PRIVATE_PATH = DATA_DIR / "pitchbook_export.csv"
FIXTURE_PATH = DATA_DIR / "synthetic_fixture.csv"

# A file whose first line contains this marker is treated as synthetic and
# everything downstream is labeled accordingly.
SYNTHETIC_MARKER = "SYNTHETIC"

REQUIRED_COLUMNS = ("sector", "quarter", "total_funding_usd", "deal_count")
OPTIONAL_COLUMNS = ("median_valuation_usd",)

# Canonical name -> lower-cased, whitespace-collapsed header spellings we accept.
COLUMN_ALIASES = {
    "sector": {"sector", "vertical", "verticals", "industry", "industry sector",
               "primary industry sector", "primary industry group"},
    "quarter": {"quarter", "period", "deal quarter", "qtr", "year quarter"},
    "total_funding_usd": {"total_funding_usd", "total funding", "total funding ($)",
                          "deal size", "sum of deal size", "capital invested",
                          "total capital invested", "capital invested ($)"},
    "deal_count": {"deal_count", "deal count", "deals", "# of deals", "number of deals",
                   "count of deals", "count"},
    "median_valuation_usd": {"median_valuation_usd", "median valuation",
                             "median valuation ($)", "median post valuation",
                             "median post-money valuation", "median post money valuation"},
}

_QUARTER_RE = re.compile(r"(?:(?P<y1>\d{4})\D{0,3}Q(?P<q1>[1-4]))|(?:Q(?P<q2>[1-4])\D{0,3}(?P<y2>\d{4}))",
                         re.IGNORECASE)


def _normalize_header(name: str) -> str:
    return re.sub(r"\s+", " ", str(name).strip().lower())


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Rename recognised header spellings to their canonical names."""
    rename = {}
    for col in df.columns:
        norm = _normalize_header(col)
        for canonical, aliases in COLUMN_ALIASES.items():
            if norm in aliases:
                rename[col] = canonical
                break
    return df.rename(columns=rename)


def parse_quarter(value) -> pd.Period:
    """Parse '2019Q3', '2019-Q3', 'Q3 2019', 'Q3-2019' into a quarterly Period."""
    if isinstance(value, pd.Period):
        return value.asfreq("Q")
    text = str(value).strip()
    m = _QUARTER_RE.search(text)
    if not m:
        raise ValueError(f"Cannot parse quarter from {value!r}")
    year = int(m.group("y1") or m.group("y2"))
    q = int(m.group("q1") or m.group("q2"))
    return pd.Period(year=year, quarter=q, freq="Q")


def _is_synthetic_file(path: Path) -> bool:
    with open(path, "r", encoding="utf-8") as fh:
        first = fh.readline()
    return SYNTHETIC_MARKER.lower() in first.lower()


def load_private(path: str | Path | None = None) -> pd.DataFrame:
    """Load the sector x quarter private-funding table.

    Resolution order when ``path`` is None: ``data/pitchbook_export.csv`` if it
    exists, otherwise the committed synthetic fixture (with a loud warning).

    Returns a DataFrame with columns
    ``sector, quarter (Period[Q]), total_funding_usd, deal_count, median_valuation_usd``
    sorted by (sector, quarter). ``df.attrs['synthetic']`` is True when the
    source file is marked synthetic; ``df.attrs['source']`` is the file path.
    """
    if path is None:
        if DEFAULT_PRIVATE_PATH.exists():
            path = DEFAULT_PRIVATE_PATH
        else:
            warnings.warn(
                "No PitchBook export found at data/pitchbook_export.csv; "
                "falling back to the SYNTHETIC fixture. Results are not meaningful.",
                stacklevel=2,
            )
            path = FIXTURE_PATH
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(path)

    synthetic = _is_synthetic_file(path)
    raw = pd.read_csv(path, comment="#")
    df = normalize_columns(raw)

    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(
            f"{path.name} is missing required columns {missing}. "
            f"Found: {list(raw.columns)}. See data/README.md for the expected schema."
        )
    for col in OPTIONAL_COLUMNS:
        if col not in df.columns:
            df[col] = np.nan

    out = pd.DataFrame({
        "sector": df["sector"].astype(str).str.strip().str.lower(),
        "quarter": df["quarter"].map(parse_quarter),
        "total_funding_usd": pd.to_numeric(df["total_funding_usd"], errors="coerce"),
        "deal_count": pd.to_numeric(df["deal_count"], errors="coerce"),
        "median_valuation_usd": pd.to_numeric(df["median_valuation_usd"], errors="coerce"),
    })

    dupes = out.duplicated(["sector", "quarter"], keep=False)
    if dupes.any():
        bad = out.loc[dupes, ["sector", "quarter"]].drop_duplicates().head(5)
        raise ValueError(f"Duplicate (sector, quarter) rows, e.g.\n{bad}")

    out = out.sort_values(["sector", "quarter"]).reset_index(drop=True)
    out.attrs["synthetic"] = synthetic
    out.attrs["source"] = str(path)
    return out


def load_synthetic_fixture() -> pd.DataFrame:
    """Load the committed FAKE fixture explicitly."""
    return load_private(FIXTURE_PATH)


# ----------------------------------------------------------------------------
# Public side
# ----------------------------------------------------------------------------

def _download_history(ticker: str, start: str) -> pd.Series:
    import yfinance as yf  # imported lazily so tests do not need network

    hist = yf.Ticker(ticker).history(start=start, auto_adjust=True)
    if hist.empty:
        raise RuntimeError(f"yfinance returned no data for {ticker}")
    close = hist["Close"].copy()
    close.index = pd.to_datetime(close.index).tz_localize(None).normalize()
    close.name = ticker
    return close


def load_prices(tickers, start: str = "2014-01-01", end: str | None = None,
                cache_dir: Path = CACHE_DIR, refresh: bool = False) -> pd.DataFrame:
    """Daily adjusted closes, one column per ticker, cached per ticker as CSV.

    The cache is keyed only on ticker and start date; pass ``refresh=True`` to
    force a re-download (for example to extend the sample to today).
    """
    cache_dir = Path(cache_dir)
    cache_dir.mkdir(parents=True, exist_ok=True)
    series = []
    for t in tickers:
        f = cache_dir / f"{t}_{start}.csv"
        if f.exists() and not refresh:
            s = pd.read_csv(f, index_col=0, parse_dates=True).iloc[:, 0]
            s.name = t
        else:
            s = _download_history(t, start)
            s.to_csv(f, header=True)
        series.append(s)
    prices = pd.concat(series, axis=1).sort_index()
    if end is not None:
        prices = prices.loc[:end]
    return prices
