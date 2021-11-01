from web_scraper import __version__ 
from web_scraper.scraper import get_citations_needed_count

def test_version():
    assert __version__ == '0.1.0'

def test_get_citations_needed_count():
    url = "https://en.wikipedia.org/wiki/History_of_Mexico"
    expected = 5
    actual = get_citations_needed_count(url)
    assert actual == expected