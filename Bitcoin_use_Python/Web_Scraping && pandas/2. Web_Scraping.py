from re import U
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/item/main.nhn?code=000660"
html = requests.get(url).text
    
soup = BeautifulSoup(html, "html5lib")
# tags = soup.select("table tbody tr td em")
# tags = soup.select(".lwidth tbody .strong td em")
# tags = soup.select("#tab_con1 > div:nth-of-type(2) > table > tbody > tr.strong > td > em")
tags = soup.select("#tab_con1 > div:nth-child(3) > table > tbody > tr.strong > td > em")

for tag in tags:
    print(tag.text)
