### 설명 ###
# 상승장과 하락장을 구분하는 방법은 이동평균보다 현가가 높다면 상승장, 그렇지 않다면 하락장으로 판단합니다.

import pybithumb

# 웹스크레핑을 통해 일봉 데이터를 가져옵니다
btc = pybithumb.get_ohlcv("BTC")
close = btc['close']
print(btc)