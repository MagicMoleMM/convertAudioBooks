import json
from contextlib import nullcontext
from dataclasses import replace
from pickletools import float8
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import openpyxl


url1 = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCRUB'
item1 = requests.get(url1)
BTCRUB = item1.json()['price']

url2 = 'https://api.binance.com/api/v3/ticker/price?symbol=ETHRUB'
item2 = requests.get(url2)
ETHRUB = item2.json()['price']

url3 = 'https://api.binance.com/api/v3/ticker/price?symbol=USDTRUB'
item3 = requests.get(url3)
USDTRUB = item3.json()['price']

url4 = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT'
item4 = requests.get(url4)
BTCUSDT = item4.json()['price']

url5 = 'https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT'
item5 = requests.get(url5)
ETHUSDT = item5.json()['price']


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
    'QIWI', 'Tinkoff'
]

tradetypes = ["SELL", "BUY"]

assets = [
    'BTC', 'ETH', 'USDT', 'RUB'
]

results = []

for paytype in paytypes:
    for tradetype in tradetypes:
        for asset in assets:

            data = {
                "asset": asset,
                "fiat": "RUB",
                "merchantCheck": False,
                "page": 1,
                "payTypes": [paytype],
                "publisherType": None,
                "rows": 1,
                "tradeType": tradetype
            }

            r = requests.post(
                'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=data)
            dt = r.json()
            results = results + [dt['data'][0]['adv']['price']]


series = [BTCRUB, ETHRUB, USDTRUB, BTCUSDT, ETHUSDT]

fin = series + results
index = ['BTCRUB', 'ETHRUB', 'USDTRUB', 'BTCUSDT', 'ETHUSDT', 'BTC_QIWI_sell', 'ETH_QIWI_sell', 'USDT_QIWI_sell', 'RUB_QIWI_sell', 'BTC_QIWI_buy', 'ETH_QIWI_buy',
         'USDT_QIWI_buy', 'RUB_QIWI_buy', 'BTC_Tinkoff_sell', 'ETH_Tinkoff_sell', 'USDT_Tinkoff_sell', 'RUB_Tinkoff_sell', 'BTC_Tinkoff_buy', 'ETH_Tinkoff_buy', 'USDT_Tinkoff_buy', 'RUB_Tinkoff_buy']
list_1 = pd.Series(fin, index=index)
list_2 = pd.to_numeric(list_1, downcast='float')
print(list_2)
list_2.to_excel('/Users/magicmole/Documents/P2P/P2P_calc.xlsx',
                sheet_name='data')
