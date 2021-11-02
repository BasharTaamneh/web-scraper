from bs4 import BeautifulSoup
import requests

def get_citations_needed_count(url):

    """
    scrapes a webpage and reports the number of citations needed.

    Arguments:
    ---

    url: String
    Return: Integer number of needed citations.
    """

    response = requests.get(url)
    # print(len(citations_needed))
    bsoup = BeautifulSoup(response.content, "html.parser")
    # print(bsoup)
    citations_needed = bsoup.find_all(class_="noprint Inline-Template Template-Fact")
    # print(response.text)
    # print(citations_needed)
    # print(len(citations_needed))
    return len(citations_needed)


def get_citations_needed_report(url: str):
    """
    scrapes a webpage and reports passages where citations needed.

    Arguments:
    ---
    url: String
    Return: Strings of passages.
    """
    response = requests.get(url)
    bsoup = BeautifulSoup(response.content, "html.parser")
    citations = bsoup.find_all("p")

    citation_for = ""
    paragraphs = []

    for citation in citations:
        if citation.find(class_="noprint Inline-Template Template-Fact"):
            scraped_text = citation.get_text()
            paragraphs.append(scraped_text.split("\n")[0])

    for text in paragraphs:
        points = text.count("[citation needed]")
        for i in range(points):
            cleaned_text = text.split("[citation needed]")
            citation_for += ("citation needed: {}\n".format(cleaned_text[i].strip()))

    # print(citation_for)
    return citation_for


# if __name__ == "__main__":
    # get_citations_needed_count('https://en.wikipedia.org/wiki/History_of_Mexico')
    # get_citations_needed_report("https://en.wikipedia.org/wiki/History_of_Mexico")
