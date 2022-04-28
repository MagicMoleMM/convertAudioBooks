import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import openpyxl


url = "https://audiokniga-onlain.ru/rus_klassik/"
page = requests.get(url)
# print(page.status_code)
soup = bs(page.content, 'html.parser')
content = soup.find(id="dle-content")

# content_item = content.find_all(class_="thumb-in")
# item = content_item[0]
# # print(item.prettify())
# book_name = item.find("img")["alt"]
# book_img = item.find("img")["data-src"]
# book_group = item.find(class_="t-meta").get_text()

pages_content = soup.find(class_="navigation")
pages = [page.get_text() for page in pages_content.select("a")]
pages1 = [page["href"] for page in pages_content.select("a")]
next_page = pages1[0]
# print(int(pages[len(pages)-1]) - 1)
# print(next_page)

books_names = [name["alt"] for name in content.select(".thumb-in img")]
books_imgs = [name["data-src"] for name in content.select(".thumb-in img")]
book_groups = [name.get_text() for name in content.select(".thumb-in .t-meta")]

i = 0
for i in range(int(pages[len(pages)-1]) - 1):
    url = "https://audiokniga-onlain.ru/rus_klassik/page/"+str(i)
    page = requests.get(url)
    soup = bs(page.content, 'html.parser')
    content = soup.find(id="dle-content")
    books_names = books_names + [name["alt"] for name in content.select(".thumb-in img")]
    books_imgs = books_imgs + [name["data-src"] for name in content.select(".thumb-in img")]
    book_groups = book_groups + [name.get_text() for name in content.select(".thumb-in .t-meta")]



books = pd.DataFrame({
    "book_name": books_names,
    "book_img": books_imgs,
    "book_group": book_groups,
    })

name = pd.Series(books_names)[0].split(' / ')
print(name)
print(books)

books.to_excel("/Users/MagicMole/PycharmProjects/FB_request/books_classic.xlsx")