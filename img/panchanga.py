import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import json

item = []
item_day = []
item_moon_day = []
item_festival = []
item_festival_title = []

for i in range(1, 13): 
    url = f'https://www.drikpanchang.com/panchang/month-panchang.html?date=01/{i}/2022'
    item = requests.get(url)
    soup = bs(item.content, 'html.parser')
    item_content = soup.find(class_="dpMonthGrid")
    

    # item_day = item_day + [page.get_text() for page in item_content.select(".dpBigDate")]
    # item_moon_day = item_moon_day + [page.get_text() for page in item_content.select(".dpSmallDate")]
    
    try:
        [page.get_text() for page in item_content.select(".dpCellFestivalName a")]
    except:
        item_festival  = item_festival + ['-']
    else:
        item_festival = item_festival + [page.get_text() for page in item_content.select(".dpCellFestivalName a")]
    
    try:
        [page.get_text() for page in item_content.select(".dpCellFestivalName a")]
    except:
        item_festival  = item_festival + ['-']
    else:
        item_festival_title = item_festival_title + [name["title"] for name in item_content.select(".dpCellFestivalName a")]


print(item_festival)
print(item_festival_title)
print(len(item_festival))
print(len(item_festival_title))

festivals = pd.DataFrame({
    "item_festival": item_festival,
    "item_festival_title": item_festival_title

})

festivals.to_csv('./festivals.csv')