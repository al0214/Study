import pybithumb
import time


tickers = pybithumb.get_tickers()
# 현재 비트코인 가격 가져오기
for ticker in tickers:
    price = pybithumb.get_current_price(ticker)
    print(f' 현재 비트코인 가격은 :{tickers}:{price}원')
    time.sleep(0.1)
