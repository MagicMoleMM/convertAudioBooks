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
    "page":1,
    "rows":10,
    "payTypes":["Tinkoff"], #"QIWI", "SBP"
    "classifies":[],
    "asset":"USDT",
    "transAmount":"20000",
    "fiat":"RUB",
    "merchantCheck":False,
    "filter":{"payTypes":[]},
    "tradeType":"BUY"
    }

headers = {
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Accept-Language': 'ru',
    'Accept-Encoding': 'gzip, deflate, br',
    'Host': 'www.pexpay.com',
    'Origin': 'https://www.pexpay.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
    'Connection': 'keep-alive',
    'Content-Length': '161',
    #'x-ui-request-trace:': 'f4e68e34-79da-45e3-8d3c-2dfe0dbffd55',
    'clienttype': 'web',
    'lang': 'en',
    'csrftoken': 'd41d8cd98f00b204e9800998ecf8427e',
    }


results_pexpay = []

url = 'https://www.pexpay.com/bapi/c2c/v1/friendly/c2c/ad/search'

r = requests.post(url, headers=headers, json=data)
dt = r.json()
#print((json.dumps(dt, indent=4)))

try:
    [dt["data"][0]["adDetailResp"]["price"]]
except:
    results_pexpay = results_pexpay + None
else:
    results_pexpay = results_pexpay + [dt["data"][0]["adDetailResp"]["price"]]

print(results_pexpay)
