import pybithumb

# ALL 인자를 넘겨 모든 가상화폐에 대한 정보를 가져올 수 있다.
all = pybithumb.get_current_price("ALL")
for k, v in all.items():
    print(k, v)
    
# Key	Description
# opening_price	    최근 24시간 내 시작 거래금액
# closing_price	    최근 24시간 내 마지막 거래금액
# min_price 최근	 24시 간 내 최저 거래금액
# max_price 최근	 24시 간 내 최고 거래금액
# average_price	    최근 24시간 내 평균 거래금액
# units_traded	    최근 24시간 내 Currency 거래량
# volume_1day	    최근 1일간 Currency 거래량
# volume_7day	    최근 7일간 Currency 거래량
# buy_price	        거래 대기건 최고 구매가
# sell_price	    거래 대기건 최소 판매가
# 24H_fluctate	    24시간 변동금액
# 24H_fluctate_rate	24시간 변동률

