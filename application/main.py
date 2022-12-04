import json, re, requests
import csv
import os
import pandas as pd
import web3
from bs4 import BeautifulSoup
from web3 import Web3
from web3.middleware import geth_poa_middleware
import urllib.request
from etherscan import Etherscan

# with open('data/0x0a6bb2770450f8bb7cc0b42ee859ac7f9177010d.json') as f:
#   data = json.load(f)

path_to_json = '../data'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

for j in json_files:
    with open('data/' + str(j)) as f:
        data = json.load(f)
        # print(data['address'])


# this function will get the chain by given address
# def get_chain(address):
#     url = 'https://api.etherscan.io/api?module=account&action=txlist&address=' + address
#     response = urllib.request.urlopen(url)
#     data = response.json()
#     return data


def get_label(address):
    url = "https://etherscan.io/address/0x388c818ca8b9251b393131c08a736a67ccb19297"
    response = urllib.request.urlopen(url)
    data = response.read()
    # print(data)
    soup = BeautifulSoup(data, 'html.parser')
    # print(soup)
    mydivs = soup.findAll("div", {"class": "text-center"})
    # print(mydivs)
    # label = soup.find_all('a', href="/accounts/label/")
    return 1


# <a class="mb-1 mb-sm-0 u-label u-label--xs u-label--info" href="/accounts/label/lido">Lido</a>
# this function will scrape json files from a given url
def get_json(path_to_json):
    url = 'https://github.com/0xTracker/ethereum-address-metadata/tree/master/data'
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a', href=re.compile('.json')):
            with open(os.path.join(path_to_json, link['href'].split('/')[-1]), 'wb') as f:
                f.write(requests.get(
                    'https://raw.githubusercontent.com/0xTracker/ethereum-address-metadata/master/data/' +
                    link['href'].split('/')[-1]).content)
    else:
        print('Error')
    # print all json files in f
    for f in os.listdir(path_to_json):
        print(f)


if __name__ == '__main__':
     address = '0x388C818CA8B9251b393131C08a736A67ccB19297'

    # # print(get_chain(address))
    # # get the chain id from web3
    # w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161'))
    # w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    # chain_id = w3.eth.chainId
    # print(chain_id)
