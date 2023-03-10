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

"""
data = {
    "userId":"",
    "tokenId":"BTC",
    "currencyId":"RUB",
    "payment":["62"], # '62' - QIWI, '75' - Tinkoff
    "side":"0", # 0/1
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
print(min(dt["result"]["count"], 10))

try:
    [dt["result"]["items"][0]["price"]]
except:
    results_bybit = results_bybit + [None]

else:
    for i in range(min(dt["result"]["count"], 10)):
        if ([dt["result"]["items"][i]["recentExecuteRate"]][0] >= 80 and [dt["result"]["items"][i]["recentOrderNum"]][0] >= 10 and [dt["result"]["items"][i]["isOnline"]][0] and [dt["result"]["items"][i]["finishNum"]][0] > 0):
            break

    if ([dt["result"]["items"][i]["recentExecuteRate"]][0] >= 80 and [dt["result"]["items"][i]["recentOrderNum"]][0] >= 10 and [dt["result"]["items"][i]["isOnline"]][0] and [dt["result"]["items"][i]["finishNum"]][0] > 0):
        results_bybit = results_bybit + [dt["result"]["items"][i]["price"]]
    else:
        results_bybit = results_bybit + [None]

print(results_bybit,i)
"""

def extract_json_objects(text, decoder=JSONDecoder()):

    pos = 0
    while True:
        match = text.find('{', pos)
        if match == -1:
            break
        try:
            result, index = decoder.raw_decode(text[match:])
            yield result
            pos = match + index
        except ValueError:
            pos = match + 1



results_huobi = []
url = 'https://otc-api.trygofast.com/v1/data/trade-market?coinId=1&currency=11&tradeType=buy&currPage=1&payMethod=69&acceptOrder=-1&country=&blockType=general&online=1&range=0&amount=20000&isThumbsUp=false&isMerchant=false&isTraded=false&onlyTradable=false&isFollowed=false'

page = requests.get(url)
with open('result.json', 'w', encoding='utf-8') as f:
    for result in extract_json_objects(page.text):
        json.dump(result, f, ensure_ascii=False, indent=4)

print(min(result['totalCount'],result['pageSize']),
        [result['data'][0]["tradeMonthTimes"]][0] > 10,
        [result['data'][0]["isOnline"]][0],
        [result['data'][0]["payTerm"]][0] <= 15,
        int([result['data'][0]["orderCompleteRate"]][0]) > 80)

try:
    [result['data'][0]["price"]]
except:
    results_huobi = results_huobi + [None]
else:
    for i in range(min(result['totalCount'],result['pageSize'])):
        if ([result['data'][i]["tradeMonthTimes"]][0] > 10 and [result['data'][i]["isOnline"]][0] and [result['data'][i]["payTerm"]][0] <= 15 and int([result['data'][i]["orderCompleteRate"]][0]) >= 85):
            break

    if ([result['data'][i]["tradeMonthTimes"]][0] > 10 and [result['data'][i]["isOnline"]][0] and [result['data'][i]["payTerm"]][0] <= 15 and int([result['data'][i]["orderCompleteRate"]][0]) >= 85):
        results_huobi = results_huobi + [result['data'][i]["price"]]
    else:
        results_huobi = results_huobi + [None]

    
print(results_huobi,i)
"""
headers_pexpay = {
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

data_pexpay = {
        "page":1,
         "rows":10,
         "payTypes":["sbpotkr"],
         "classifies":[],
         "asset":"BNB",
         "transAmount":"20000",
         "fiat":"RUB",
         "merchantCheck":False,
         "filter":{"payTypes":[]},
         "tradeType":"SELL"
            }

results_pexpay = []
        
url_pexpay = 'https://www.pexpay.com/bapi/c2c/v1/friendly/c2c/ad/search'

r_pexpay = requests.post(url_pexpay, headers=headers_pexpay, json=data_pexpay)
dt_pexpay = r_pexpay.json()
#print((json.dumps(dt_pexpay, indent=4)))

try:
    [dt_pexpay["data"][0]["adDetailResp"]["price"]]
except:
    results_pexpay = results_pexpay + [None]
else:
    for i in range(min(len(dt_pexpay["data"]),10)):
        if ([dt_pexpay["data"][i]["advertiserVo"]["userStatsRet"]["completedSellOrderNumOfLatest30day"]][0] > 10 and 
            [dt_pexpay["data"][i]["advertiserVo"]["userStatsRet"]["finishRateLatest30day"]][0] > 0.80 and 
            [dt_pexpay["data"][i]["advertiserVo"]["makerOnlineStatus"]["status"]][0] == "on"):
            break
    if ([dt_pexpay["data"][i]["advertiserVo"]["userStatsRet"]["completedSellOrderNumOfLatest30day"]][0] > 10 and 
        [dt_pexpay["data"][i]["advertiserVo"]["userStatsRet"]["finishRateLatest30day"]][0] > 0.80 and 
        [dt_pexpay["data"][i]["advertiserVo"]["makerOnlineStatus"]["status"]][0] == "on"):
        results_pexpay = results_pexpay + [dt_pexpay["data"][0]["adDetailResp"]["price"]]
    else:
        results_pexpay = results_pexpay + [None]


print(results_pexpay,i)


print(dt_pexpay["data"][0]["advertiserVo"]["makerOnlineStatus"]["status"])


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

data = {
    "proMerchantAds":False,
    "page":1,
    "rows":10,
    "payTypes":["TinkoffNew"],
    "countries":[],
    "publisherType":None,
    "transAmount":"50000",
    "asset":"ETH",
    "fiat":"RUB",
    "tradeType":"BUY"
    }

results =[]

r = requests.post(
    'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=data)
dt = r.json()
#print((json.dumps(dt, indent=4)))

try:
    [dt['data'][0]['adv']['price']]
except:
    results = results + [None]

else:
    for i in range(min(len(dt["data"]),10)):
        if ([dt["data"][i]["advertiser"]["monthOrderCount"]][0] > 10 and 
            [dt["data"][i]["advertiser"]["monthFinishRate"]][0] > 0.80):

            break
    if ([dt["data"][i]["advertiser"]["monthOrderCount"]][0] > 10 and 
        [dt["data"][i]["advertiser"]["monthFinishRate"]][0] > 0.80):
        results = results + [dt['data'][i]['adv']['price']]
    else:
        results = results + [None]

print(results,i)

def spot_binance(simbol):
    url = f'https://api.binance.com/api/v3/ticker/price?symbol={simbol}'
    item = requests.get(url)
    simbol = float(item.json()['price'])
    return simbol

spot = [
    'BTCRUB',
    'USDTRUB',
    'ETHRUB',
    'XRPRUB',
    'LTCRUB',
    'TRXUSDT',
    'BNBRUB',
    'BUSDRUB',
    'SHIBUSDT',
]

spot_copy = spot

USDTRUB = spot_binance('USDTRUB')

spot_kurs = []

for n in spot:
    if n[-3:] == 'RUB':
        spot_kurs = spot_kurs + [spot_binance(n)]
    else:
        spot_kurs = spot_kurs + [spot_binance(n) * USDTRUB]

print(spot_kurs)
"""