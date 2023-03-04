from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selenium import webdriver
import lxml
import time
import re
import requests


deposit = 20000

assets = [
        #'BTC',
        #'ETH',
        'USDT',   
    ]

tradetypes = [
            "SELL",
            "BUY",
            #"SELL", 
            ]


for asset in assets:
    for tradetype in tradetypes:

        link = f'https://www.huobi.com/ru-ru/fiat-crypto/trade/{tradetype}-{asset}-rub/'
        browser = webdriver.Chrome()
        browser.get(link)

        try:
            WebDriverWait(browser, 10).until(EC.presence_of_element_located(
                (By.CLASS_NAME, "trade-page-container")))

            #browser.find_element(By.CSS_SELECTOR, 'pay-search-container span').click()
            #browser.find_element(By.CSS_SELECTOR, 'span.val_QIWI').click() #span.val_Tinkoff
            #browser.find_element(By.CSS_SELECTOR, 'div.marketSelectNav-sellnum-main input').send_keys(str(deposit))
            #browser.find_element(By.CSS_SELECTOR, 'div.marketSelectNav button').click()

            time.sleep(2)

            crypt_elements = browser.find_elements(By.CLASS_NAME, 'otc-trade-list')
            prices_html = bs(crypt_elements[0].get_attribute('innerHTML'), features='lxml').prettify()

        # Запишем разметку в html файл
            with open("huobi.html","w") as f:
                print(prices_html, file=f)

        # Базовый try catch для проверки ошибок.    
        except Exception as e:
            print(e)

        finally:

            time.sleep(2)
            # закрываем браузер после всех манипуляций
            browser.quit()

   
        soup = bs(prices_html, 'html.parser')
        rate = soup.find(class_='price').get_text()

        def get_num(x):
            return float(''.join(ele for ele in x if ele.isdigit() or ele == '.'))

        rate_ = get_num(rate)

        print(rate_)

   