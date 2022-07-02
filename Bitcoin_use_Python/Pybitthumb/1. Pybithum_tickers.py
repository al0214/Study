import pybithumb 

# 빗썸은 세 자리 이상의 대문자를 사용해서 가상화폐를 구분하는데 이를 티커라고 한다.
tickers = pybithumb.get_tickers()
print(f'총 티커의 개수는 : {len(tickers)}')
