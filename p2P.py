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

    #send_text = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chatID}&parse_mode=Markdown&text={bot_message}'
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

def job():

    deposit = 20000

    url1 = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCRUB'
    item1 = requests.get(url1)
    BTCRUB = item1.json()['price']

    url2 = 'https://api.binance.com/api/v3/ticker/price?symbol=ETHRUB'
    item2 = requests.get(url2)
    ETHRUB = item2.json()['price']

    url3 = 'https://api.binance.com/api/v3/ticker/price?symbol=USDTRUB'
    item3 = requests.get(url3)
    USDTRUB = item3.json()['price']

    url4 = 'https://api.binance.com/api/v3/ticker/price?symbol=BNBRUB'
    item4 = requests.get(url4)
    BNBRUB = item4.json()['price']

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
        #'x-ui-request-trace:': 'f4e68e34-79da-45e3-8d3c-2dfe0dbffd55',
        'clienttype': 'web',
        'lang': 'en',
        'csrftoken': 'd41d8cd98f00b204e9800998ecf8427e',
        }

    paytypes = [
        #'Advcash',
        #'RUBfiatbalance',
        'TinkoffNew',
        #'YandexMoneyNew',
        'QIWI',
        'RosBankNew',
    ]

    for paytype in paytypes:

        coins = {1,2,3,-1}
        method = int

        trades = {
            #'sell',
            'buy',
            }
        
        if paytype == 'TinkoffNew':
            method = 28
        if paytype == 'QIWI':
            method = 9
        if paytype == 'RosBankNew':
            method = 69
        
        results_huobi = []
        
        for coin in coins:
            for trade in trades:

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
                    if ([result['data'][0]["tradeMonthTimes"]][0] == 0 or [result['data'][0]["payTerm"]][0] > 15):
                        if ([result['data'][1]["tradeMonthTimes"]][0] == 0 or [result['data'][1]["payTerm"]][0] > 15):
                            results_huobi = results_huobi + [result['data'][2]["price"]]
                        else:
                            results_huobi = results_huobi + [result['data'][1]["price"]]
                    else:
                        results_huobi = results_huobi + [result['data'][0]["price"]]

        tradetypes = [
                    "SELL", 
                    #"BUY",
                    ]

        assets = [
            #'RUB',
            'BTC',
            'USDT',
            'ETH',
            'BNB',
        ]

        results = []
        trademethod = []
        trade = []
        fiatUnit = []
        assetUnit = []
        results_bybit = []
        results_pexpay = []
        payment = []
        payment_pexpay = []

        if paytype == 'TinkoffNew':
            payment_pexpay = ["Tinkoff"]
        if paytype == 'QIWI':
            payment_pexpay = ["QIWI"]
        if paytype == 'RosBankNew':
            payment_pexpay = ['SBP']

        for asset in assets:

            data_pexpay = {
                "page":1,
                "rows":10,
                "payTypes":payment_pexpay, #"QIWI", "SBP"
                "classifies":[],
                "asset":asset,
                "transAmount":str(deposit),
                "fiat":"RUB",
                "merchantCheck":False,
                "filter":{"payTypes":[]},
                "tradeType":"SELL"
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
                if ([dt_pexpay["data"][0]["advertiserVo"]["userStatsRet"]["completedOrderNum"]][0] < 10.0 or [dt_pexpay["data"][0]["advertiserVo"]["userStatsRet"]["finishRate"]][0] < 0.60):
                    if ([dt_pexpay["data"][1]["advertiserVo"]["userStatsRet"]["completedOrderNum"]][0] < 10.0 or [dt_pexpay["data"][1]["advertiserVo"]["userStatsRet"]["finishRate"]][0] < 0.60):
                        results_pexpay = results_pexpay + [dt_pexpay["data"][2]["adDetailResp"]["price"]]
                    else:
                        results_pexpay = results_pexpay + [dt_pexpay["data"][1]["adDetailResp"]["price"]]
                else:
                    results_pexpay = results_pexpay + [dt_pexpay["data"][0]["adDetailResp"]["price"]]


        if paytype == 'TinkoffNew':
            payment = ["75"]
        if paytype == 'QIWI':
            payment = ["62"]
        if paytype == 'RosBankNew':
            payment = ["14"]

        for asset in assets:

            data_bybit = {
                "userId":"",
                "tokenId":asset,
                "currencyId":"RUB",
                "payment": payment,
                "side":"0", 
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
                if ([dt_["result"]["items"][0]["recentExecuteRate"]][0] <= 60 ):
                    if ([dt_["result"]["items"][1]["recentExecuteRate"]][0] <= 60 ):
                        results_bybit = results_bybit + [dt_["result"]["items"][2]["price"]]
                    else:
                        results_bybit = results_bybit + [dt_["result"]["items"][1]["price"]]
                else:
                    results_bybit = results_bybit + [dt_["result"]["items"][0]["price"]]



        for asset in assets:
            for tradetype in tradetypes:
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
                            results = results + [None]
                            trademethod = trademethod + [None]
                            trade = trade + [None]
                            assetUnit = assetUnit + [None]
                            fiatUnit = fiatUnit + [None]
                        else:
                            results = results + [dt['data'][0]['adv']['price']]
                            trademethod = trademethod + [dt['data'][0]['adv']['tradeMethods'][0]['tradeMethodName']]
                            trade = trade + [dt['data'][0]['adv']['tradeType']]
                            assetUnit = assetUnit + [dt['data'][0]['adv']['asset']]
                            fiatUnit = fiatUnit + [dt['data'][0]['adv']['fiatUnit']]


        series = [
                #1, 
                BTCRUB,
                USDTRUB,
                ETHRUB, 
                BNBRUB,
            ]

        dt_pd = pd.DataFrame({
            "trademethod": paytype,
            "assetUnit": assetUnit,
            "trade": 'Вывод',
            "binance": results,
            "huobi": results_huobi,
            "bybit": results_bybit,
            "pexpay": results_pexpay,
            "spot": series,   
        })

        dt_pd['binance'] = dt_pd['binance'].astype(float)
        dt_pd['huobi'] = dt_pd['huobi'].astype(float)
        dt_pd['bybit'] = dt_pd['bybit'].astype(float)
        dt_pd['pexpay'] = dt_pd['pexpay'].astype(float)
        dt_pd['spot'] = dt_pd['spot'].astype(float)
        dt_pd['percent_binance'] = (dt_pd['binance'] - dt_pd['spot']*1.012)/(dt_pd['spot']*1.012)*100
        dt_pd['percent_huobi'] = (dt_pd['huobi'] - dt_pd['spot']*1.012)/(dt_pd['spot']*1.012)*100
        dt_pd['percent_bybit'] = (dt_pd['bybit'] - dt_pd['spot']*1.012)/(dt_pd['spot']*1.012)*100
        dt_pd['percent_pexpay'] = (dt_pd['pexpay'] - dt_pd['spot']*1.012)/(dt_pd['spot']*1.012)*100
        dt_pd['profit_binance'] = np.round(dt_pd['percent_binance'] * deposit / 100,decimals=2)
        dt_pd['profit_huobi'] = np.round(dt_pd['percent_huobi'] * deposit / 100,decimals=2)
        dt_pd['profit_bybit'] = np.round(dt_pd['percent_bybit'] * deposit / 100,decimals=2)
        dt_pd['profit_pexpay'] = np.round(dt_pd['percent_pexpay'] * deposit / 100,decimals=2)
        #dt_pd['good_price'] = np.round((dt_pd['binance'] * 1.0001), decimals=3)
        #dt_pd['good_loss'] = np.round((((1.012 * dt_pd['spot']) - (dt_pd['binance'] * 1.0001)) / (dt_pd['binance'] * 1.0001) * 100),decimals=2)

        status_0 = dt_pd[['percent_binance','percent_huobi','percent_bybit','percent_pexpay']].max().max()
        status_1 = dt_pd[['percent_binance','percent_huobi','percent_bybit','percent_pexpay']].max().values
        status = f"максимальный процент  - {np.round(status_0,decimals=2)}%"
        status_ = f"Диапазон значений  - {np.round(status_1,decimals=2)}%"

        profit = np.round(deposit * status_0 / 100, decimals=2)
        
        columns = {
            'percent_binance',
            'percent_huobi',
            'percent_bybit',
            'percent_pexpay',
        }

        for column in columns:
            row = dt_pd.index[dt_pd[column] == dt_pd[['percent_binance','percent_huobi','percent_bybit','percent_pexpay']].max().max()].tolist()
            if row != []:
                column_ = column.replace('percent_', '')
                price_ = dt_pd[column_][row].values[0]
                active = dt_pd['assetUnit'][row].values[0]
                pay_method = dt_pd['trademethod'][row].values[0]
                text = f'Лучшая продажа - {active} по цене {price_}.\nПлатежный метод - {pay_method}, биржа - {column_},  \n{status}.\nProfit {profit} / Deposit {deposit}. \n{status_}'
                

        if status_0 > 2.0:
            telegram_bot_sendtext(text)
            time.sleep(5)

job()

#schedule.every().hour.at(":01").do(job)
schedule.every(20).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
