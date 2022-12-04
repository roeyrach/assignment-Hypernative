import datetime
import requests
import bs4
import csv
import time

SECONDS = 5


def get_data_from_address():
    url = "https://docs.uniswap.org/contracts/v3/reference/deployments"
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
                                                        '(KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'})
    page_soup = bs4.BeautifulSoup(response.content, "html.parser")
    tbody = page_soup.find_all("tbody")[1]
    children = tbody.findChildren("tr", recursive=False)
    with open('csv_file_updates_Q2.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Chain", "Address", "Label"])
    file.close()
    for child in children:
        columns = []
        counter = 0
        for td in child.findChildren("td", recursive=False):
            if counter == 1:
                counter += 1
                continue
            columns.append(td.text)
            counter += 1
        with open('csv_file_updates_Q2.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([columns[0], columns[1], columns[2]])
        file.close()


def timer(seconds):
    while True:
        get_data_from_address()
        print("last check at", datetime.datetime.now().strftime("%D %H:%M:%S"))
        time.sleep(seconds)


if __name__ == '__main__':
    timer(SECONDS)
