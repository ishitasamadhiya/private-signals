"""Sector -> ETF mapping.

PitchBook's taxonomy and public sector ETFs do not line up one-to-one, so this
mapping is a judgment call. It lives in one place so it can be argued with.

How each study sector is sourced from PitchBook (see scripts/convert_pitchbook_pivot.py):

    study sector    PitchBook dimension            label                      ETF
    technology      Primary Industry Sector        Information Technology     XLK
    healthcare      Primary Industry Sector        Healthcare                 XLV
    financials      Primary Industry Sector        Financial Services         XLF
    energy          Primary Industry Sector        Energy                     XLE
    industrials     Primary Industry Sector        B2B (Business Products
                                                   and Services)              XLI
    software        Primary Industry Group         Software                   IGV
    semiconductors  Primary Industry Group         Semiconductors             SMH
    biotech         Primary Industry Code          Biotechnology              XBI
    cybersecurity   Vertical                       Cybersecurity              HACK
    fintech         Vertical                       FinTech                    FINX

Known looseness, stated up front:
* "industrials" uses PitchBook's whole B2B sector, which is broader than XLI
  (it includes business services and commercial products of all kinds).
* Verticals are multi-valued tags, so a deal can count toward both
  cybersecurity and fintech, and toward its primary sector as well.
* The ten series therefore overlap (software is inside technology, biotech
  inside healthcare, fintech straddles technology and financials). The
  cross-sectional sorts treat them as ten separate sectors anyway; overlap
  works against finding a spread, not for it.
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
