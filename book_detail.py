import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import openpyxl

url = "https://audiokniga-onlain.ru/lubov_fentezi/"
page = requests.get(url)
soup = bs(page.content, 'html.parser')
content = soup.find(id="dle-content")
pages_content = soup.find(class_="navigation")
pages = [page.get_text() for page in pages_content.select("a")]
links_url = [name["href"] for name in content.select(".thumb-img")]

for i in range(2, int(pages[-1])+1):
    url = "https://audiokniga-onlain.ru/lubov_fentezi/page/" + str(i)
    page = requests.get(url)
    soup = bs(page.content, 'html.parser')
    content_url = soup.find(id="dle-content")
    links_url = links_url + [name["href"] for name in content_url.select(".thumb-img")]

book_names = []
book_authors = []
books_mp3 = []
book_readers = []
book_series = []
book_group = []
books_img = []

for url in links_url:
    url_page = url
    page = requests.get(url_page)
    soup = bs(page.content, 'html.parser')
    content = soup.find(id="dle-content")
    content_item = content.find(class_="full")
    book_names = book_names + [content_item.find("h1").get_text()]
    book_authors = book_authors + [content_item.find_all("a")[0].get_text()]
    books_img = books_img + [name["src"] for name in content_item.select("img")]
    # try:
    #     book_readers = book_readers + [content_item.find_all("a")[1].get_text()]
    #     book_series = book_series + [content_item.find("u").get_text()]
    #     book_group = book_group + [content_item.find_all("a")[2].get_text()]
    #
    # except IndexError:
    #     pass
    # except AttributeError:
    #     pass


    book_mp3_content = content_item.select(".dleaudioplayer ul li")
    links_mp3 = []
    for link in book_mp3_content:
        links_mp3.append(link.get('data-url'))
    books_mp3 = books_mp3 + [links_mp3]



books = pd.DataFrame({
    "book_name": book_names,
    "book_author": book_authors,
    "books_mp3": books_mp3,
    "books_img": books_img,
    # "book_reader": book_readers,
    # "book_series": book_series,
    # "book_group": book_group,

    })




books.to_excel("/Users/MagicMole/PycharmProjects/FB_request/love_fantasy.xlsx")
