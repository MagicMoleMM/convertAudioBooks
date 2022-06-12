import requests
from bs4 import BeautifulSoup as bs
import random




user_agent_list = [
    # Chrome
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
    # Firefox
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0'
]

urls = [  # "https://rutube.ru/channel/25868408/videos/",
    # "https://rutube.ru/channel/25868408/videos/page-2/",
    # "https://rutube.ru/channel/25868408/videos/page-3/",
    # "https://rutube.ru/channel/25868408/videos/page-4/",
    # "https://rutube.ru/channel/25868408/videos/page-5/",
    # "https://rutube.ru/channel/25868408/videos/page-6/",
    # "https://rutube.ru/channel/25868408/videos/page-7/",
    # "https://rutube.ru/channel/25868408/videos/page-8/",
    # "https://rutube.ru/channel/25868408/videos/page-9/",
    # "https://rutube.ru/channel/25868408/videos/page-10/",
    # "https://rutube.ru/channel/25868408/videos/page-11/",
    # "https://rutube.ru/channel/25868408/videos/page-12/",
    # "https://rutube.ru/channel/25868408/videos/page-13/",
    # "https://rutube.ru/channel/25868408/videos/page-14/",
    "https://audiokniga-onlain.ru",

]


links = []
i = 0

page = ''

# headers = random.choice(user_agent_list)
headers = {
    'User-Agent': random.choice(user_agent_list)
}
with requests.Session() as s:
    page = s.get("https://rutube.ru/channel/25868408/videos/page-9/")
    print(page.status_code)


# for url in urls:
#     while page == '':
#         try:
#             headers = random.choice(user_agent_list)
#             with requests.Session() as s:
#                 page = s.get(url, headers=headers)
#                 print(page.status_code)
#                 # soup = bs(page.content, 'html.parser')
#                 # content = soup.find(class_="wdp-grid-module__grid")
#                 # links = links + [name["href"] for name in content.select("section > a")]
#             break
#         except:
#             print("Connection refused by the server..")
#             print("Let me sleep for 5 seconds")
#             print("ZZzzzz...")
#             time.sleep(5)
#             print("Was a nice sleep, now let me continue...")
#             continue


# print(links)
# print(len(links))
