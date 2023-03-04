import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import json

item = []
item_day = []
item_moon_day = []
item_festival = []
item_festival_title = []
item_sunrise = []
item_sunset = []

for i in range(1, 13): 
    url = f'https://www.drikpanchang.com/panchang/month-panchang.html?geoname-id=4477893&date=01/{i}/2023' # manteo 
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
        item_festival_title  = item_festival_title + ['-']
    else:
        item_festival_title = item_festival_title + [name["title"] for name in item_content.select(".dpCellFestivalName a")]

    try:
        [page.get_text() for page in item_content.select(".dpSunriseTiming")]
    except:
        item_sunrise  = item_sunrise + ['-']
    else:
        item_sunrise = item_sunrise + [page.get_text() for page in item_content.select(".dpSunriseTiming")]

    try:
        [page.get_text() for page in item_content.select(".dpSunsetTiming")]
    except:
        item_sunset  = item_sunset + ['-']
    else:
        item_sunset = item_sunset + [page.get_text() for page in item_content.select(".dpSunsetTiming")]

    # try:
    #     [page.get_text() for page in item_content.select("div[data-url]")]
    # except:
    #     item_day  = item_day + ['-']
    # else:
    #     item_day = item_day + [page.get_text() for page in item_content.select("div[data-url]")]

    try:
        [name["data-url"] for name in item_content.select(".dpMonthGridCell")]
    except:
        item_day  = item_day + ['-']
    else:
        item_day = item_day + [name["data-url"] for name in item_content.select(".dpMonthGridCell")]

# print(item_sunrise)
# print(item_sunset)
# print(item_day)
print(len(item_sunrise))
print(len(item_festival))
print(len(item_day))

festivals = pd.DataFrame({
    "item_festival": item_festival,
    "item_festival_title": item_festival_title,
    #  "item_sunset": item_sunset,

})

festivals.to_csv('./manteo_2023.csv')