import pybithumb

# ALL 인자를 넘겨 모든 가상화폐에 대한 정보를 가져올 수 있다.
all = pybithumb.get_current_price("ALL")
for k, v in all.items()
    print(k, v)
