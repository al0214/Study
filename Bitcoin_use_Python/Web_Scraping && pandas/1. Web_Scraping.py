# 웹 크롤링과 웹 스크래핑이란? 
# 웹 서버에 저장된 데이터를 가져오는 행위이다.

# 일반적으로 특정한 데이터만을 웹사이트로부터 가져오는 행위를 스크래핑 ( 다수의 사람들이 하는 것 (이것을 웹 크롤링이라고 오해하고 있다.))
# 웹 크롤링은 구글, 네이버, 다음과 같은 포털 사이트들이 인터넷에 있는 다수의 정보를 가져가는 행위
# 포털 사이트에서 대규모의 웹 데이터를 가져가는 것을 웹 크롤링이다.

# 기본 방식
# url = "http://naver.com"
# response = requests.get(url)

from re import U
import requests
from bs4 import BeautifulSoup
# BeautifulSoup 객체는 HTML 파싱을 위한 다양한 메서드를 갖고 있습니다

def get_per(code):
    url = "https://finance.naver.com/item/main.nhn?code=000660"
    html = requests.get(url).text
    
    soup = BeautifulSoup(html, "html5lib")
    tags = soup.select("#_per")
    tag = tags[0]
    return float(tag.text)

def get_dividend(code):
    url = "https://finance.naver.com/item/main.nhn?code=000660"
    html = requests.get(url).text
    
    soup = BeautifulSoup(html, "html5lib")
    tags = soup.select("#_dvr")
    tag = tags[0]
    return float(tag.text)

print(f'per 값 : {print(get_per("00060"))}')
print(f'배당 수익률 : {print(get_dividend("00060"))}')
