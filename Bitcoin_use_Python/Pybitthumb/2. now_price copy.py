import pybithumb
import time

# 현재 비트코인 가격 가져오기
while True:
    price = pybithumb.get_current_price("BTC")
    print(f' 현재 비트코인 가격은 : {price}원 입니다')
    time.sleep(1)
