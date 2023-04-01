import json
import time
import requests
import pandas as pd
import numpy as np
from json import JSONDecoder
import schedule

def telegram_bot_sendtext(bot_message):
    
    bot_token = '6265667740:AAGu0tMfeMe09gD_YL0klKuNmH9OiQsVX9I'
    bot_chatID = '@P2P_magic'

    send_text = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chatID}&text={bot_message}'
    response = requests.get(send_text)

    return response.json()

def extract_json_objects(text, decoder=JSONDecoder()):
    """Find JSON objects in text, and yield the decoded JSON data
    Does not attempt to look for JSON arrays, text, or other JSON types outside
    of a parent JSON object.
    """
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

def spot_binance (simbol):
    url = f'https://api.binance.com/api/v3/ticker/price?symbol={simbol}'
    item = requests.get(url)
    simbol = float(item.json()['price'])
    return simbol

deposit = 30000

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

headers_bybit = {
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
    'clienttype': 'web',
    'lang': 'en',
    'csrftoken': 'd41d8cd98f00b204e9800998ecf8427e',
    }

paytypes = [
    'TinkoffNew',
    'RosBankNew',
    'QIWI',
    'SBP',  
]

assets = [
    'BTC',
    'USDT',
    'ETH',
    'XRP',
    'LTC',
    'TRX',
    'BNB',
    'BUSD',
    'SHIB',
]
tradetypes = [
    "SELL", 
    "BUY",
    ]

for tradetype in tradetypes:

    results = []
    trademethod = []
    #trade = []
    assetUnit = []
    results_bybit = []
    results_pexpay = []
    payment = []
    payment_pexpay = []
    paytype_ = []
    results_huobi = []
    spot_kurs =[]

    coins =  [1,2,3,7,8,22,-1,-2,-3,]
    method = int
    trade = str
    
    for paytype in paytypes:

        if tradetype == "SELL":
            trade = 'buy'
        else:
            trade = 'sell'
        
        if paytype == 'TinkoffNew':
            method = 28
        if paytype == 'QIWI':
            method = 9
        if paytype == 'SBP':
            method = 69
        if paytype == 'RosBankNew':
            method =29

        for coin in coins:

            url = f'https://otc-api.trygofast.com/v1/data/trade-market?coinId={coin}&currency=11&tradeType={trade}&currPage=1&payMethod={method}&acceptOrder=-1&country=&blockType=general&online=1&range=0&amount={deposit}&isThumbsUp=false&isMerchant=false&isTraded=false&onlyTradable=false&isFollowed=false'
            
            page = requests.get(url)
            with open('result.json', 'w', encoding='utf-8') as f:
                for result in extract_json_objects(page.text):
                    json.dump(result, f, ensure_ascii=False, indent=4)
            
            try:
                [result['data'][0]["price"]]
            except:
                results_huobi = results_huobi + [None]
            else:
                for i in range(min(result['totalCount'],result['pageSize'])):
                    if ([result['data'][i]["tradeMonthTimes"]][0] > 10 and 
                        [result['data'][i]["isOnline"]][0] and [result['data'][i]["payTerm"]][0] <= 20 and 
                        int([result['data'][i]["orderCompleteRate"]][0]) >= 85):

                        break

                if ([result['data'][i]["tradeMonthTimes"]][0] > 10 and [result['data'][i]["isOnline"]][0] and 
                    [result['data'][i]["payTerm"]][0] <= 20 and 
                    int([result['data'][i]["orderCompleteRate"]][0]) >= 85):
                    results_huobi = results_huobi + [result['data'][i]["price"]]
                else:
                    results_huobi = results_huobi + [None]


        if paytype == 'TinkoffNew':
            payment_pexpay = ["Tinkoff"]
        if paytype == 'QIWI':
            payment_pexpay = ["QIWI"]
        if paytype == 'SBP':
            payment_pexpay = ['SBP']
        if paytype == 'RosBankNew':
            payment_pexpay = ['Sberbank']

        for asset in assets:

            data_pexpay = {
                "page":1,
                "rows":10,
                "payTypes":payment_pexpay, 
                "classifies":[],
                "asset":asset,
                "transAmount":str(deposit),
                "fiat":"RUB",
                "merchantCheck":False,
                "filter":{"payTypes":[]},
                "tradeType":tradetype
                }
            
            url_pexpay = 'https://www.pexpay.com/bapi/c2c/v1/friendly/c2c/ad/search'

            r_pexpay = requests.post(url_pexpay, headers=headers_pexpay, json=data_pexpay)
            dt_pexpay = r_pexpay.json()
            #print((json.dumps(dt, indent=4)))

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
                    results_pexpay = results_pexpay + [dt_pexpay["data"][i]["adDetailResp"]["price"]]
                else:
                    results_pexpay = results_pexpay + [None]


        if paytype == 'TinkoffNew':
            payment = ["75"]
        if paytype == 'QIWI':
            payment = ["62"]
        if paytype == 'SBP':
            payment = ["382"]
        if paytype == 'RosBankNew':
            payment = ["185"]

        if tradetype == 'SELL':
            side = '0',
        else:
            side = '1'

        for asset in assets:

            data_bybit = {
                "userId":"",
                "tokenId":asset,
                "currencyId":"RUB",
                "payment": payment,
                "side":side, 
                "size":"10",
                "page":"1",
                "amount": str(deposit),
                }
            
            url = 'https://api2.bybit.com/fiat/otc/item/online'

            r = requests.post(url, headers=headers_bybit, json=data_bybit)
            dt_ = r.json()

            try:
                [dt_["result"]["items"][0]["price"]]
            except:
                results_bybit = results_bybit + [None]
            else:
                for i in range(min(dt_["result"]["count"], 10)):
                    if ([dt_["result"]["items"][i]["recentExecuteRate"]][0] >= 80 and 
                        [dt_["result"]["items"][i]["recentOrderNum"]][0] >= 10 and [dt_["result"]["items"][i]["isOnline"]][0] and 
                        [dt_["result"]["items"][i]["finishNum"]][0] > 0):
                        break

                if ([dt_["result"]["items"][i]["recentExecuteRate"]][0] >= 80 and 
                    [dt_["result"]["items"][i]["recentOrderNum"]][0] >= 10 and [dt_["result"]["items"][i]["isOnline"]][0] and 
                    [dt_["result"]["items"][i]["finishNum"]][0] > 0):
                    results_bybit = results_bybit + [dt_["result"]["items"][i]["price"]]
                else:
                    results_bybit = results_bybit + [None]


        for asset in assets:

            data = {
                "asset": asset,
                "fiat": "RUB",
                "merchantCheck": False,
                "page": 1,
                "payTypes": [paytype],
                "publisherType": None,
                "rows": 10,
                "tradeType": tradetype,
                "transAmount":  str(deposit),
            }

            r = requests.post(
                'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=data)
            dt = r.json()
            #print((json.dumps(dt, indent=4)))
            try:
                [dt['data'][0]['adv']['price']]
            except:
                results = results + [None]
                paytype_ = paytype_ + [paytype]
                assetUnit = assetUnit + [asset]
            else:
                for i in range(min(len(dt["data"]),10)):
                    if ([dt["data"][i]["advertiser"]["monthOrderCount"]][0] > 10 and 
                        [dt["data"][i]["advertiser"]["monthFinishRate"]][0] > 0.80):
                        break

                if ([dt["data"][i]["advertiser"]["monthOrderCount"]][0] > 10 and 
                    [dt["data"][i]["advertiser"]["monthFinishRate"]][0] > 0.80):

                    results = results + [dt['data'][i]['adv']['price']]
                    paytype_ = paytype_ + [paytype]
                    assetUnit = assetUnit + [asset]
                else:
                    results = results + [None]
                    paytype_ = paytype_ + [paytype]
                    assetUnit = assetUnit + [asset]

        USDTRUB = spot_binance('USDTRUB')
        for n in spot:
            if n[-3:] == 'RUB':
                spot_kurs = spot_kurs + [spot_binance(n)]
            else:
                spot_kurs = spot_kurs + [spot_binance(n) * USDTRUB]
        
    dt_pd = pd.DataFrame({
        "trademethod": paytype_,
        "assetUnit": assetUnit,
        "trade": tradetype,
        "binance": results,
        "huobi": results_huobi,
        "bybit": results_bybit,
        "pexpay": results_pexpay,
        "spot": spot_kurs,   
    })

    dt_pd['binance'] = dt_pd['binance'].astype(float)
    dt_pd['huobi'] = dt_pd['huobi'].astype(float)
    dt_pd['bybit'] = dt_pd['bybit'].astype(float)
    dt_pd['pexpay'] = dt_pd['pexpay'].astype(float)
    dt_pd['spot'] = dt_pd['spot'].astype(float)
    dt_pd['percent_binance'] = (dt_pd['binance'] - dt_pd['spot'])/(dt_pd['spot'])*100
    dt_pd['percent_huobi'] = (dt_pd['huobi'] - dt_pd['spot'])/(dt_pd['spot'])*100
    dt_pd['percent_bybit'] = (dt_pd['bybit'] - dt_pd['spot'])/(dt_pd['spot'])*100
    dt_pd['percent_pexpay'] = (dt_pd['pexpay'] - dt_pd['spot'])/(dt_pd['spot'])*100
    dt_pd['profit_binance'] = np.round(dt_pd['percent_binance'] * deposit / 100,decimals=2)
    dt_pd['profit_huobi'] = np.round(dt_pd['percent_huobi'] * deposit / 100,decimals=2)
    dt_pd['profit_bybit'] = np.round(dt_pd['percent_bybit'] * deposit / 100,decimals=2)
    dt_pd['profit_pexpay'] = np.round(dt_pd['percent_pexpay'] * deposit / 100,decimals=2)

    with pd.ExcelWriter("/Users/magicmole/Documents/Binance/P2P_sber.xlsx", mode='a', if_sheet_exists='replace', engine="openpyxl") as writer:  
        dt_pd.to_excel(writer, sheet_name=f"Вывод {tradetype}")
    
    