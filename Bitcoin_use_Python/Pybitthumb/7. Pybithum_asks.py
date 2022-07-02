import pybithumb

orderbook = pybithumb.get_orderbook("BTC")
asks = orderbook["asks"]

for ask in asks:
    price = ask['price']
    quant = ask['quantity']
    print(f"매도호가 : {price}, 매도잔량 : {quant}")