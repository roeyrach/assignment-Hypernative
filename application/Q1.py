import re, requests
import csv
from bs4 import BeautifulSoup
import threading

json_files = []
json_data = []


# get the json files from the website
def get_json():
    # get all json files from url
    url = 'https://github.com/0xTracker/ethereum-address-metadata/tree/master/data'
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a', href=re.compile('.json')):
            url1 = "https://raw.githubusercontent.com" + link.get('href')
            blob = url1.split('/blob')
            url2 = blob[0] + blob[1]
            json_files.append(url2)


# decode json file
def decode_json(line, index):
    response = requests.get(line)
    data = response.json()
    json_data.append((data, index))


# create a csv file to store the data
def json_to_csv():
    with open('application/csv_file_Q1.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Chain", "Address", "Label"])
    for j in json_data:
        with open('application/csv_file_Q1.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ethereum', j[0]['address'], j[0]['name']])


if __name__ == '__main__':
    get_json()
    threads = []
    for i in range(len(json_files)):
        t = threading.Thread(target=decode_json, args=(json_files[i], i))
        t.start()
        threads.append(t)
    for i in range(len(json_files)):
        threads[i].join()
    json_data = sorted(json_data, key=lambda x: x[1])
    json_to_csv()
    print("csv is Done")
