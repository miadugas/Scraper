import requests
from bs4 import BeautifulSoup
# to give an interval between multiple requests
import time
# csv import
import csv

urls = ["https://finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch", "https://finance.yahoo.com/quote/FB?p=FB", "https://finance.yahoo.com/quote/TWTR?p=TWTR&.tsrc=fin-srch", "https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch"]

# putting this in to make it appear that a browser is making the query's and not a bot :p
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36' }

for url in urls:
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

    table_info = soup.find_all("div", class_="D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)")[0].find_all("tr")

    for i in range(0,8):
        heading = table_info[i].find_all("td")[0].get_text()
        # print()
        value = table_info[i].find_all("td")[1].get_text()

        print(heading + " : " + value)
    
    # sleep for 7 seconds before next request
    time.sleep(7)