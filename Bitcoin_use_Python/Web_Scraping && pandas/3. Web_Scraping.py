import requests
import datetime

r = requests.get("https://api.korbit.co.kr/v1/ticker/detailed?currency_pair=btc_krw")

print(f'\nr의 타입 {type(r.text)}')

bitcoin = r.json()

print(f'{bitcoin}\n bitcoin의 타입 {type(bitcoin)}')
print(f'last의 값 추출 : {bitcoin["last"]}')
print(f'bid의 값 추출 : {bitcoin["bid"]}')
print(f'ask의 값 추출 : {bitcoin["ask"]}')
print(f'volume의 값 추출 : {bitcoin["volume"]}')

timastamp = bitcoin["timestamp"]
date = datetime.datetime.fromtimestamp(timastamp / 1000)
print(date)
