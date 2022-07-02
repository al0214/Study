import pybithumb
import datetime

orderbook = pybithumb.get_orderbook("BTC")
print(orderbook)

for k in orderbook:
    print(k)
# timestamp
# payment_currency
# order_currency
# bids
# asks

print(f"현재 빗썸 거래시 통화는 : {orderbook['payment_currency']} 입니다.")
print(f"지금 조회하신 티커는 : {orderbook['order_currency']} 입니다.")

# 매도 호가를 asks라고 부르고 매수 호가를 bids라고 부릅니다
ms = int(orderbook["timestamp"])
dt = datetime.datetime.fromtimestamp(ms / 1000)
print(f"조회하신 매도 호가는 {orderbook['asks']}이며,\n매수 호가는 {orderbook['bids']}입니다.\n 조회하신 시간은 : {dt} 입니다")

