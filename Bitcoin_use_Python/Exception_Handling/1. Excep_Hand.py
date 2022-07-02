price = {"open" : 100, "high" : 150, "low" : 90, "close" : 130}

## 예외 처리 전 ##
print("point-1")
open = price['open1']
print("point-2")

## 예외 처리 후 ##
try:
    open = price["open1"]
except:
    pass