import pybithumb

# 저가 / 고가 / 거래금액 / 거리량을 가져옵니다. ( 형태는 튜플로 )
detail = pybithumb.get_market_detail("BTC")
print(detail)