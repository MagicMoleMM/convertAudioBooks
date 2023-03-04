import json
from contextlib import nullcontext
from dataclasses import replace
from pickletools import float8
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import openpyxl


headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Length": "123",
    "content-type": "application/json",
    "Host": "p2p.binance.com",
    "Origin": "https://p2p.binance.com",
    "Pragma": "no-cache",
    "TE": "Trailers",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"
}

paytypes = [
    'Advcash',
    #'RUBfiatbalance',
    #'TinkoffNew',
    #'QIWI',
    #'RosBankNew',
    ]

tradetypes = [
            "SELL", 
            #"BUY",
            ]

assets = [
    'BTC',
    #'ETH',
    #'BNB',
    #'USDT',
    
]


data = {
    "asset": 'BTC',
    "fiat": "RUB",
    #"merchantCheck": True,
    "merchantCheck": False,
    "page": 4,
    #"payTypes": [paytype],
    "payTypes": [],
    #"publisherType": 'merchant',
    "publisherType": None,
    "rows": 3,
    "tradeType": "SELL",
    #"transAmount":  "10000",
}

r = requests.post(
    'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=data)
dt = r.json()
print((json.dumps(dt, indent=4)))
print(r.request.body)