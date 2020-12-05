import requests
from bs4 import BeautifulSoup

url = "https://finance.yahoo.com/quote/GOOGL?p=GOOGL&.tsrc=fin-srch"

# putting this in to make it appear that a browser is making the query's and not a bot :p
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36' }

html_page = requests.get(url, headers=headers)
# pass the parser, lxml is the fastest so I'm using that
soup = BeautifulSoup(html_page.content, 'lxml')

# If I want to grab the page title
# print(soup.title)

# extract page title and drop the tags
# title = soup.find("title").get_text()
# print(title)
header_info = soup.find_all("div", id="quote-header-info")[0]
stock_title = header_info.find("h1").get_text()
current_price = header_info.find("div", class_="My(6px) Pos(r) smartphone_Mt(6px)").find("span").get_text()

print(stock_title)
print(current_price)