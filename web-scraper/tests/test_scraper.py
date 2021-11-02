from web_scraper import __version__ 
from web_scraper.scraper import get_citations_needed_count, get_citations_needed_report

def test_version():
    assert __version__ == '0.1.0'

def test_get_citations_needed_count():
    url = "https://en.wikipedia.org/wiki/History_of_Mexico"
    expected = 5
    actual = get_citations_needed_count(url)
    assert actual == expected

def test_get_citations_needed_report():
    url = "https://en.wikipedia.org/wiki/History_of_Mexico"
    out_report = get_citations_needed_report(url)
    actual = out_report.split(":")[1]

    expected =""" The first people to settle in Mexico encountered a climate far milder than the current one. In particular, the Valley of Mexico contained several large paleo-lakes (known collectively as Lake Texcoco) surrounded by dense forest. Deer were found in this area, but most fauna were small land animals and fish and other lacustrine animals were found in the lake region.
citation needed"""
    assert actual == expected
