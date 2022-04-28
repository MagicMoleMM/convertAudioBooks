from selenium import webdriver
from selenium.webdriver.common.proxy import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import time
import os

# PROXY = '177.93.41.158:999'
PROXY = '151.106.13.222:1080'

options = Options()
options.add_argument('--proxy-server=http://%s' % PROXY)
driver = webdriver.Chrome(options=options, executable_path=os.path.abspath("/Users/MagicMole/Downloads/chromedriver"))
try:
    # driver.get('http://icanhazip.com')
    driver.get('https://rutube.ru/video/22ac4a151350c906a6fb9f41977a8b23/')
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR, '[action="play"]').click()
    time.sleep(30)
    driver.quit()
except:
    print('Captcha!')




# 58.27.59.249:80
# Страница запроса с IP: 1.9.74.142
# Статус код: 200

