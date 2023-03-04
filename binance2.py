import json
from contextlib import nullcontext
from dataclasses import replace
from pickletools import float8
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
import openpyxl

deposit = 30000

url1 = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCRUB'
item1 = requests.get(url1)
BTCRUB = item1.json()['price']

url2 = 'https://api.binance.com/api/v3/ticker/price?symbol=ETHRUB'
item2 = requests.get(url2)
ETHRUB = item2.json()['price']

url3 = 'https://api.binance.com/api/v3/ticker/price?symbol=USDTRUB'
item3 = requests.get(url3)
USDTRUB = item3.json()['price']

'''
url4 = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT'
item4 = requests.get(url4)
BTCUSDT = item4.json()['price']

url5 = 'https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT'
item5 = requests.get(url5)
ETHUSDT = item5.json()['price']
'''

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
    #'Advcash',
    #'YandexMoneyNew',
    #'RUBfiatbalance',
    'TinkoffNew',
    'QIWI',
    #'RosBankNew',
    
    
]

for paytype in paytypes:


    tradetypes = [
                "SELL", 
                #"BUY",
                ]

    assets = [
        'BTC',
        'ETH',
        'USDT',
        'RUB',
    ]

    results = []
    trademethod = []
    trade = []
    fiatUnit = []
    assetUnit = []

    for asset in assets:
        for tradetype in tradetypes:
            #for paytype in paytypes:
                for i in range(1,2):
                    for j in range(1,2):

                        data = {
                            "asset": asset,
                            "fiat": "RUB",
                            #"merchantCheck": True,
                            "merchantCheck": False,
                            "page": i,
                            "payTypes": [paytype],
                            #"payTypes": [],
                            #"publisherType": 'merchant',
                            "publisherType": None,
                            "rows": j,
                            "tradeType": tradetype,
                            "transAmount":  str(deposit),
                        }

                        r = requests.post(
                            'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=data)
                        dt = r.json()
                        #print((json.dumps(dt, indent=4)))
                        if [dt['data'][0]['adv']['price']] == None:
                            results = results + ['0']
                            trademethod = trademethod + ['0']
                            trade = trade + ['0']
                            assetUnit = assetUnit + ['0']
                            fiatUnit = fiatUnit + ['0']
                        else:
                            results = results + [dt['data'][0]['adv']['price']]
                            trademethod = trademethod + [dt['data'][0]['adv']['tradeMethods'][0]['tradeMethodName']]
                            trade = trade + [dt['data'][0]['adv']['tradeType']]
                            assetUnit = assetUnit + [dt['data'][0]['adv']['asset']]
                            fiatUnit = fiatUnit + [dt['data'][0]['adv']['fiatUnit']]


    series = [BTCRUB, 
        ETHRUB, 
        USDTRUB, 
        1,
        ]

    dt_pd = pd.DataFrame({
        "trademethod": trademethod,
        "trade": trade,
        "results": results,
        "spot": series,
        "assetUnit": assetUnit,
        "fiatUnit": fiatUnit,
        
    })

    dt_pd['results'] = dt_pd['results'].astype(float)
    dt_pd['spot'] = dt_pd['spot'].astype(float)
    #dt_pd['percent'] = ((dt_pd['results'] - dt_pd['spot'] * 1.012)/(dt_pd['spot'] * 1.012))*100
    dt_pd['percent'] = ((dt_pd['results'] - dt_pd['spot'] * 1.012)/(dt_pd['spot'] * 1.012))*100
    dt_pd['profit'] = np.round(dt_pd['percent'] * deposit / 100,decimals=2)
    dt_pd['good_price'] = np.round((dt_pd['results'] * 1.0001), decimals=3)
    dt_pd['good_loss'] = np.round((((1.012 * dt_pd['spot']) - (dt_pd['results'] * 1.0001)) / (dt_pd['results'] * 1.0001) * deposit),decimals=2)

    print(dt_pd)

#dt_pd.to_excel("/Users/magicmole/Documents/Binance/Binance.xlsx")




