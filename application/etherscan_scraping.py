import requests
import bs4


def get_data_from_address(address):
    url = f"https://etherscan.io/address/{address}#code"
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                                                        '(KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'})
    page_soup = bs4.BeautifulSoup(response.content, "html.parser")
    labels = []
    for finding in page_soup.find_all("div", {"class": "mt-1"}):
        children = finding.findChildren("a", recursive=False)
        for child in children:
            labels.append(child.text)
    for finding in page_soup.find_all("div",
                                      {"class": "card-header d-flex justify-content-between align-items-center"}):
        children = finding.findChildren("div", recursive=False)
        for child in children:
            for finding2 in child.find_all("span"):
                children2 = finding2.findChildren("span", recursive=False)
                for child2 in children2:
                    labels.append(child2.text)
    return labels

