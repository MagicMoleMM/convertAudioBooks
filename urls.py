import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


urls = ["https://rutube.ru/channel/25868408/videos/",
        "https://rutube.ru/channel/25868408/videos/page-2/",
        "https://rutube.ru/channel/25868408/videos/page-3/",
        "https://rutube.ru/channel/25868408/videos/page-4/",
        "https://rutube.ru/channel/25868408/videos/page-5/",
        "https://rutube.ru/channel/25868408/videos/page-6/",
        "https://rutube.ru/channel/25868408/videos/page-7/",
        "https://rutube.ru/channel/25868408/videos/page-8/",
        "https://rutube.ru/channel/25868408/videos/page-9/",
        "https://rutube.ru/channel/25868408/videos/page-10/",
        "https://rutube.ru/channel/25868408/videos/page-11/",
        "https://rutube.ru/channel/25868408/videos/page-12/",
        "https://rutube.ru/channel/25868408/videos/page-13/",
        "https://rutube.ru/channel/25868408/videos/page-14/",
        
        ]

links = []
i = 0

for url in urls:

    page = requests.get(url)
    soup = bs(page.content, 'html.parser')
    content = soup.find(class_="wdp-grid-module__grid")
    links = links + [name["href"] for name in content.select("section > a")]

print(links)
print(len(links))
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver = webdriver.Safari()
driver.set_window_size(1024, 600)
# driver.maximize_window()

for link in links:

    link = random.choice(links)

    try:
        driver.get(link)
        time.sleep(30)
        driver.find_element(By.CSS_SELECTOR, '[action="play"]').click()
        time.sleep(random.randint(40, 70))
        print(link)
        print(i)

    except:
        pass

    i = i + 1

driver.quit()

# http://icanhazip.com
# 219.100.37.238

