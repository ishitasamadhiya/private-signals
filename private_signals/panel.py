"""Build the sector x quarter panel joining funding features to forward returns.

Timing convention
-----------------
Funding activity in quarter *t* is treated as known at the end of quarter *t*.
Forward returns are measured from the last trading day of quarter *t + lag*
to the last trading day of quarter *t + lag + h*, for horizon *h* in quarters.
``lag=0`` is the base case; ``lag=1`` is a robustness check that allows for
PitchBook's reporting delay (deals are often added weeks after they close).

Return modes
------------
* ``raw``     simple price return of the sector ETF
* ``excess``  raw return minus beta x market (SPY) return, with beta estimated
              from trailing daily returns ending at the signal date (no lookahead)
* ``vol_adj`` excess return divided by trailing annualised volatility of the
              ETF, so that returns are in risk units comparable across sectors
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from .sectors import MARKET_ETF, SECTOR_MAP

HORIZONS = (1, 2, 4)
FEATURES = ("funding_growth_qoq", "deal_growth_qoq", "funding_growth_yoy")
RETURN_MODES = ("raw", "excess", "vol_adj")


def quarter_end_prices(prices: pd.DataFrame) -> pd.DataFrame:
    """Last available close in each calendar quarter, indexed by Period[Q].

    The final quarter is dropped if the price series ends before that quarter
    does, so an in-progress quarter never masquerades as a completed one.
    """
    q = prices.resample("QE").last()
    q.index = q.index.to_period("Q")
    # A quarter counts as complete if prices run to within a few calendar days of
    # its end (the last trading day can fall up to ~4 days early around holidays).
    last_date = prices.index.max()
    if last_date < q.index[-1].end_time.normalize() - pd.Timedelta(days=4):
        q = q.iloc[:-1]
    return q


def trailing_beta(prices: pd.DataFrame, market: str = MARKET_ETF, window: int = 252) -> pd.DataFrame:
    """Rolling OLS beta of each column's daily returns on the market's daily returns."""
    rets = np.log(prices).diff()
    m = rets[market]
    cov = rets.rolling(window, min_periods=window // 2).cov(m)
    var = m.rolling(window, min_periods=window // 2).var()
    beta = cov.div(var, axis=0)
    return beta.drop(columns=[market])


def trailing_vol(prices: pd.DataFrame, window: int = 252) -> pd.DataFrame:
    """Rolling annualised volatility of daily log returns."""
    rets = np.log(prices).diff()
    return rets.rolling(window, min_periods=window // 2).std() * np.sqrt(252)


def forward_returns(prices: pd.DataFrame, horizons=HORIZONS, mode: str = "raw",
                    market: str = MARKET_ETF, window: int = 252) -> dict[int, pd.DataFrame]:
    """Forward h-quarter returns from each quarter end.

    Returns ``{h: DataFrame}`` indexed by signal quarter with one column per
    ETF (market column excluded). Row ``t`` of horizon ``h`` is the return
    from the end of quarter ``t`` to the end of quarter ``t + h``.
    """
    if mode not in RETURN_MODES:
        raise ValueError(f"mode must be one of {RETURN_MODES}")
    qp = quarter_end_prices(prices)
    etfs = [c for c in qp.columns if c != market]
    out = {}
    if mode != "raw":
        beta_q = quarter_end_prices(trailing_beta(prices, market, window))
    if mode == "vol_adj":
        vol_q = quarter_end_prices(trailing_vol(prices, window))
    for h in horizons:
        fwd = qp.shift(-h) / qp - 1.0
        if mode == "raw":
            r = fwd[etfs]
        else:
            r = fwd[etfs] - beta_q[etfs].mul(fwd[market], axis=0)
            if mode == "vol_adj":
                # scale to the horizon so units are "sigmas over h quarters"
                r = r / (vol_q[etfs] * np.sqrt(h / 4.0))
        out[h] = r
    return out


def funding_features(private: pd.DataFrame) -> pd.DataFrame:
    """Per-sector funding features from the raw sector x quarter table.

    Growth features are log-differences, which are approximately stationary and
    symmetric, unlike raw dollar changes that are dominated by the largest sector.
    """
    df = private.sort_values(["sector", "quarter"]).copy()
    g = df.groupby("sector", sort=False)
    df["log_funding"] = np.log1p(df["total_funding_usd"])
    df["log_deals"] = np.log1p(df["deal_count"])
    df["funding_growth_qoq"] = g["log_funding"].diff(1)
    df["funding_growth_yoy"] = g["log_funding"].diff(4)
    df["deal_growth_qoq"] = g["log_deals"].diff(1)
    return df


def build_panel(private: pd.DataFrame, prices: pd.DataFrame, horizons=HORIZONS,
                mode: str = "raw", lag: int = 0, sector_map: dict | None = None) -> pd.DataFrame:
    """Join funding features (signal quarter t) to forward returns from quarter t + lag.

    Rows whose sector has no ETF in ``sector_map`` are dropped with a printed
    note. Forward-return columns are named ``fwd_1q``, ``fwd_2q``, ``fwd_4q``.
    """
    sector_map = SECTOR_MAP if sector_map is None else sector_map
    feats = funding_features(private)
    unknown = sorted(set(feats["sector"]) - set(sector_map))
    if unknown:
        print(f"[panel] dropping sectors with no ETF mapping: {unknown}")
        feats = feats[feats["sector"].isin(sector_map)]
    feats["etf"] = feats["sector"].map(sector_map)

    fwd = forward_returns(prices, horizons, mode=mode)
    pieces = []
    for h, wide in fwd.items():
        long = wide.stack(future_stack=True).rename(f"fwd_{h}q").reset_index()
        long.columns = ["ret_quarter", "etf", f"fwd_{h}q"]
        pieces.append(long.set_index(["ret_quarter", "etf"]))
    fwd_long = pd.concat(pieces, axis=1).reset_index()

    feats["ret_quarter"] = feats["quarter"] + lag
    panel = feats.merge(fwd_long, on=["ret_quarter", "etf"], how="left")
    panel.attrs.update(private.attrs)
    panel.attrs["mode"] = mode
    panel.attrs["lag"] = lag
    return panel.sort_values(["quarter", "sector"]).reset_index(drop=True)
