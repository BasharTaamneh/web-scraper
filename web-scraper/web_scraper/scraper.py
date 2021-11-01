
from bs4 import BeautifulSoup
import requests

def get_citations_needed_count(url):

    """
    get_citations_needed_count function web scrapes a webpage and reports the number of citations needed.
    Arguments: 
    url: String
    Return: Integer number of needed citations.
    """

    response  = requests.get(url)
    # print(len(citations_needed))
    soup = BeautifulSoup(response.content, "html.parser")
    # print(soup)
    citations_needed = soup.find_all(class_ = "noprint Inline-Template Template-Fact")
    # print(response.text)
    return len(citations_needed)




# def get_citations_needed_report(url:str):
#     """
#     get_citations_needed_report function web scrapes a webpage and reports passages where citations are needed.
#     Arguments: 
#     url: String
#     Return: Strings of preceding passages.
#     """
#     separate_text = []
#     output_string = ""

#     wiki_page = requests.get(url)
#     soup = BeautifulSoup(wiki_page.content, "html.parser")

#     citations = soup.find_all("p")
#     for citation in citations:
#         if citation.find(class_ = "noprint Inline-Template Template-Fact"):
#             scraped_text = citation.get_text()
#             separate_text.append(scraped_text.split("\n")[0])

#     for text in separate_text:
#         prints = text.count("[citation needed]")
#         for i in range(prints):
#             cleaned_text = text.split("[citation needed]")
#             output_string += "Citation needed for : " + "'" + cleaned_text[i].strip() + "'" + "\n"

#     print(output_string)
#     return output_string

# if __name__ == "__main__":
#     get_citations_needed_count('https://en.wikipedia.org/wiki/History_of_Mexico')
