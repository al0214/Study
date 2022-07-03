import pybithumb

orderbook = pybithumb.get_orderbook("BTC")
bids = orderbook["bids"]

for bid in bids:
    price = bid['price']
    quant = bid['quantity']
    print(f"매수호가 : {price}, 매수잔량 : {quant}")