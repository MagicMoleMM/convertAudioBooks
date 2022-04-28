from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

links = [
    'https://www.avito.ru/moskva/odezhda_obuv_aksessuary/tufli_zhenskie_rachel_zoe_2348701103',
    'https://www.avito.ru/moskva/odezhda_obuv_aksessuary/tufli_zhenskie_fabiani_2348505836',
    'https://www.avito.ru/moskva/odezhda_obuv_aksessuary/sumka_zhenskaya_bcbgmaxazria_2348114507',
    'https://www.avito.ru/moskva/odezhda_obuv_aksessuary/sumka_zhenskaya_neiman_marcus_2348381554',
]
i = 0
driver = webdriver.Safari()
# driver.set_window_size(1024, 600)
driver.maximize_window()

for n in range(30):

    for link in links:
        link = random.choice(links)
        try:
            driver.get(link)
            # driver.find_element(By.CSS_SELECTOR, 'img').click()
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(random.randint(10, 20))
            driver.find_element(By.CSS_SELECTOR, '.title-info-icon-views').click()
            time.sleep(random.randint(10, 20))
            print(link)
            print(i)
        except:
            pass
        i = i + 1

driver.quit()

# <i class="title-info-icon-views"></i>