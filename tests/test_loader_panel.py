import numpy as np
import pandas as pd
import pytest

from private_signals.loader import (
    FIXTURE_PATH,
    load_private,
    load_synthetic_fixture,
    normalize_columns,
    parse_quarter,
)
from private_signals.panel import (
    build_panel,
    forward_returns,
    funding_features,
    quarter_end_prices,
)


@pytest.mark.parametrize("text", ["2019Q3", "2019-Q3", "Q3 2019", "Q3-2019", "2019 q3"])
def test_parse_quarter_variants(text):
    assert parse_quarter(text) == pd.Period("2019Q3", freq="Q")


def test_parse_quarter_rejects_garbage():
    with pytest.raises(ValueError):
        parse_quarter("third quarter of 2019-ish")


def test_normalize_columns_maps_pitchbook_style_headers():
    df = pd.DataFrame(columns=["Primary Industry Sector", " Deal Quarter", "Capital Invested", "# of Deals"])
    out = normalize_columns(df)
    assert list(out.columns) == ["sector", "quarter", "total_funding_usd", "deal_count"]


def test_synthetic_fixture_is_marked_and_well_formed():
    df = load_synthetic_fixture()
    assert df.attrs["synthetic"] is True
    assert df.attrs["source"].endswith("synthetic_fixture.csv")
    assert set(df.columns) == {"sector", "quarter", "total_funding_usd", "deal_count", "median_valuation_usd"}
    assert not df.duplicated(["sector", "quarter"]).any()
    assert df["sector"].nunique() == 10
    with open(FIXTURE_PATH) as fh:
        assert "FAKE" in fh.readline()


def test_load_private_rejects_missing_columns(tmp_path):
    p = tmp_path / "bad.csv"
    p.write_text("sector,quarter\nsoftware,2019Q1\n")
    with pytest.raises(ValueError, match="missing required columns"):
        load_private(p)


def test_load_private_rejects_duplicate_rows(tmp_path):
    p = tmp_path / "dup.csv"
    p.write_text("sector,quarter,total_funding_usd,deal_count\nsoftware,2019Q1,1,1\nsoftware,2019Q1,2,2\n")
    with pytest.raises(ValueError, match="Duplicate"):
        load_private(p)


def _toy_prices():
    # two ETFs plus market, daily, 3 full years. AAA grows deterministically so
    # forward returns are exactly computable; SPY is a seeded random walk and BBB
    # is exactly twice SPY (identical log returns, so beta = 1 and zero excess).
    idx = pd.bdate_range("2020-01-01", "2022-12-31")
    n = len(idx)
    a = 100 * (1.001 ** np.arange(n))
    m = 100 * np.exp(np.cumsum(np.random.default_rng(0).normal(0, 0.01, n)))
    b = 2 * m
    return pd.DataFrame({"AAA": a, "BBB": b, "SPY": m}, index=idx)


def test_quarter_end_prices_drops_incomplete_quarter():
    prices = _toy_prices().loc[:"2022-11-15"]   # Q4 2022 incomplete
    q = quarter_end_prices(prices)
    assert q.index[-1] == pd.Period("2022Q3", freq="Q")
    full = quarter_end_prices(_toy_prices())
    assert full.index[-1] == pd.Period("2022Q4", freq="Q")


def test_forward_returns_match_price_ratios():
    prices = _toy_prices()
    q = quarter_end_prices(prices)
    fwd = forward_returns(prices, horizons=(1, 2), mode="raw")
    t = pd.Period("2020Q2", freq="Q")
    assert fwd[1].loc[t, "AAA"] == pytest.approx(q.loc[t + 1, "AAA"] / q.loc[t, "AAA"] - 1)
    assert fwd[2].loc[t, "BBB"] == pytest.approx(q.loc[t + 2, "BBB"] / q.loc[t, "BBB"] - 1)
    assert "SPY" not in fwd[1].columns
    # last rows have no forward window
    assert np.isnan(fwd[1].iloc[-1]["AAA"]) and np.isnan(fwd[2].iloc[-2]["AAA"])


def test_excess_return_is_zero_for_an_etf_that_tracks_the_market():
    prices = _toy_prices()
    exc = forward_returns(prices, horizons=(1, 4), mode="excess")
    for h in (1, 4):
        col = exc[h]["BBB"].dropna()
        assert len(col) >= 4
        assert np.allclose(col, 0.0, atol=1e-10)
    # vol-adjusted mode divides by a positive trailing vol, so still zero for BBB
    va = forward_returns(prices, horizons=(1,), mode="vol_adj")[1]["BBB"].dropna()
    assert np.allclose(va, 0.0, atol=1e-10)


def test_funding_features_are_per_sector_log_diffs():
    private = pd.DataFrame({
        "sector": ["a", "a", "a", "b", "b", "b"],
        "quarter": pd.period_range("2020Q1", "2020Q3", freq="Q").tolist() * 2,
        "total_funding_usd": [1e9, 2e9, 4e9, 5e9, 5e9, 10e9],
        "deal_count": [10, 20, 40, 5, 5, 5],
        "median_valuation_usd": np.nan,
    })
    f = funding_features(private).set_index(["sector", "quarter"])
    q2 = pd.Period("2020Q2", freq="Q")
    assert f.loc[("a", q2), "funding_growth_qoq"] == pytest.approx(np.log1p(2e9) - np.log1p(1e9))
    assert f.loc[("b", q2), "funding_growth_qoq"] == pytest.approx(0.0)
    assert np.isnan(f.loc[("a", pd.Period("2020Q1", freq="Q")), "funding_growth_qoq"])
    # first quarter of sector b must not inherit sector a's last value
    assert np.isnan(f.loc[("b", pd.Period("2020Q1", freq="Q")), "funding_growth_qoq"])


def test_build_panel_aligns_signal_quarter_with_forward_window_and_lag():
    prices = _toy_prices()
    quarters = pd.period_range("2020Q1", "2022Q4", freq="Q")
    private = pd.DataFrame({
        "sector": ["alpha"] * len(quarters) + ["beta"] * len(quarters),
        "quarter": list(quarters) * 2,
        "total_funding_usd": np.linspace(1e9, 2e9, len(quarters)).tolist() * 2,
        "deal_count": 10,
        "median_valuation_usd": np.nan,
    })
    smap = {"alpha": "AAA", "beta": "BBB"}
    fwd = forward_returns(prices, horizons=(1, 2, 4), mode="raw")

    p0 = build_panel(private, prices, mode="raw", lag=0, sector_map=smap)
    row = p0[(p0.sector == "alpha") & (p0.quarter == pd.Period("2020Q3", freq="Q"))].iloc[0]
    assert row["fwd_1q"] == pytest.approx(fwd[1].loc[pd.Period("2020Q3", freq="Q"), "AAA"])

    p1 = build_panel(private, prices, mode="raw", lag=1, sector_map=smap)
    row = p1[(p1.sector == "alpha") & (p1.quarter == pd.Period("2020Q3", freq="Q"))].iloc[0]
    assert row["fwd_1q"] == pytest.approx(fwd[1].loc[pd.Period("2020Q4", freq="Q"), "AAA"])
    assert p1.attrs["lag"] == 1 and p1.attrs["mode"] == "raw"
