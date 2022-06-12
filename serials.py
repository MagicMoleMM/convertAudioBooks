import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import json

url = "https://zetseriali.online/serial/"
page = requests.get(url)
soup = bs(page.content, 'html.parser')

content = soup.find(id="dle-content")
pages_content = soup.find(class_="bottom-nav")

links_url =  []
titles =  [page.get_text() for page in content.select(".short-title")]

pages_link = [name["href"] for name in pages_content.select('a')][0]
pages_num = [page.get_text() for page in pages_content.select('a')][-1]


for i in range(1, 5): # int(page_num)
    url_page_link = 'https://zetseriali.online/serial/page/' + str(i)
    page = requests.get(url_page_link)
    links_url =  links_url + [name["href"] for name in content.select(".short-title")]

item_title = []
item_title_eng = []
item_year = []
item_country = []
item_translate = []
item_producer = []
item_time = []
item_genre = []
item_studio = []
item_actors = []
item_text = []
item_video_link = []
item_video_trailer = []
item_img = []
item_rating = []

for url in links_url:

    url_item = url
    item = requests.get(url_item)
    soup = bs(item.content, 'html.parser')
    item_content = soup.find(id="dle-content")

    item_title = item_title + [page.get_text() for page in item_content.select(".short-header h1")]
    item_title_eng = item_title_eng + [page.get_text() for page in item_content.select(".short-header span")]
    item_year = item_year + [[page.get_text() for page in item_content.select(".short-list a")][0]]
    item_country = item_country + [[page.get_text() for page in item_content.select(".short-list a")][1]]
    item_translate = item_translate + [[page.get_text() for page in item_content.select(".short-list li")][2]]
    item_producer = item_producer + [[page.get_text() for page in item_content.select(".short-list li")][3]]
    item_time = item_time + [[page.get_text() for page in item_content.select(".short-list li")][4]]
    item_genre = item_genre + [[page.get_text() for page in item_content.select(".short-list li")][5]]
    item_studio = item_studio + [[page.get_text() for page in item_content.select(".short-list li")][6]]
    
    try:
        item_actors = item_actors + [[page.get_text() for page in item_content.select(".short-list li")][7]]
    except IndexError:
        item_actors = item_actors + ['-']

    item_text = item_text + [[page.get_text() for page in item_content.select(".ftext p")][0]]
    item_video_link = item_video_link + [[name["src"] for name in item_content.select('.fplayer iframe')][0]]
    item_video_trailer = item_video_trailer + [[name["src"] for name in item_content.select('.fplayer iframe')][1]]
    item_img = item_img + [name["src"] for name in item_content.select('.fimg img')]
    item_rating = item_rating + [page.get_text() for page in item_content.select('.fimg div')]


print(item_title)
print(item_title_eng)
print(item_year)
print(item_country)
print(item_translate)
print(item_producer)
print(item_time)
print(item_genre)
print(item_studio)
print(item_actors)
print(item_text)
print(item_video_link)
print(item_video_trailer)
print(item_img)
print(item_rating)
print(len(item_title))
print(len(item_title_eng))
print(len(item_year))
print(len(item_country))
print(len(item_translate))
print(len(item_producer))
print(len(item_time))
print(len(item_genre))
print(len(item_studio))
print(len(item_actors))
print(len(item_text))
print(len(item_video_link))
print(len(item_video_trailer))
print(len(item_img))
print(len(item_rating))

# serials = pd.DataFrame({
#     "item_title": item_title,
#     "item_title_eng": item_title_eng,
#     "item_year": item_year,
#     "item_country": item_country,
#     "item_translate": item_translate,
#     "item_producer": item_producer,
#     "item_time": item_time,
#     "item_genre": item_genre,
#     "item_studio": item_studio,
#     "item_actors": item_actors,
#     "item_text": item_text,
#     "item_video_link": item_video_link,
#     "item_video_trailer": item_video_trailer,
#     "item_img": item_img,
#     "item_rating": item_rating,

# })

# print(serials)
# serials.to_json('./serials.json', orient="index")

# with open('./serials.json', 'r', encoding='utf-8') as f:
#     data = json.load(f)

# with open('data.json', 'w', encoding='utf-8') as f:
#     json.dump(data, f, ensure_ascii=False, indent=4)