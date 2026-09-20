"""Sector -> ETF mapping.

PitchBook verticals and public sector ETFs do not line up one-to-one, so this
mapping is a judgment call. It lives in one place so it can be argued with and
edited to match however the PitchBook export was built.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Sector:
    key: str
    etf: str
    description: str


SECTORS = (
    Sector("software", "IGV", "Application and infrastructure software (iShares Expanded Tech-Software)"),
    Sector("cybersecurity", "HACK", "Cybersecurity (Amplify Cybersecurity, formerly ETFMG Prime Cyber)"),
    Sector("biotech", "XBI", "Biotechnology, equal-weighted (SPDR S&P Biotech)"),
    Sector("semiconductors", "SMH", "Semiconductors (VanEck Semiconductor)"),
    Sector("fintech", "FINX", "Financial technology (Global X FinTech)"),
    Sector("technology", "XLK", "Broad technology (Technology Select Sector SPDR)"),
    Sector("healthcare", "XLV", "Broad health care (Health Care Select Sector SPDR)"),
    Sector("financials", "XLF", "Broad financials (Financial Select Sector SPDR)"),
    Sector("energy", "XLE", "Energy (Energy Select Sector SPDR)"),
    Sector("industrials", "XLI", "Industrials (Industrial Select Sector SPDR)"),
)

SECTOR_MAP = {s.key: s.etf for s in SECTORS}
ETF_TO_SECTOR = {s.etf: s.key for s in SECTORS}
MARKET_ETF = "SPY"
