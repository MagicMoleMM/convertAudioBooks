import json
from contextlib import nullcontext
from dataclasses import replace
from pickletools import float8
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
from IPython.display import display
import openpyxl
from json import JSONDecoder

data = {
    "userId":"",
    "tokenId":"USDT",
    "currencyId":"RUB",
    "payment":["62"], # '62' - QIWI, '75' - Tinkoff
    "side":"1", # 0/1
    "size":"10",
    "page":"1",
    "amount":"20000",
    }

headers = {
    'Accept': 'application/json',
    'Accept-Language': 'ru-RU',
    'Accept-Encoding': 'gzip, deflate, br',
    'Host': 'api2.bybit.com',
    'Origin': 'https://www.bybit.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
    'Connection': 'keep-alive',
    'Referer': 'https://www.bybit.com/',
    'Content-Length': '114',
    }

results_bybit = []

url = 'https://api2.bybit.com/fiat/otc/item/online'

r = requests.post(url, headers=headers, json=data)
dt = r.json()
#print((json.dumps(dt, indent=4)))

try:
    [dt["result"]["items"][0]["price"]]
except:
    results_bybit = results_bybit + ['0']
else:
    results_bybit = results_bybit + [dt["result"]["items"][0]["price"]]

print(results_bybit)