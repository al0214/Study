import pybithumb

# ALL 인자를 넘겨 모든 가상화폐에 대한 정보를 가져올 수 있다.
all = pybithumb.get_current_price("ALL")
for ticker, data in all.items():
    # 전 종목 현재가 불러오기 
    print(f"조회하신 티커는 {ticker} {data['closing_price']}원 입니다.")
