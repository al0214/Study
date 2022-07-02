import pybithumb
import time

## 예외 처리 방법 1번째
while True:
    price = pybithumb.get_current_price("BTC")
    if price is not None:
        print(price / 10)
    time.sleep

## 예외 처리 방법 2번째
while True:
    price = pybithumb.get_current_price("BTC")
    try:
        print(price/10)
    except:
        print("에러 발생", price)
    time.sleep(0.2)