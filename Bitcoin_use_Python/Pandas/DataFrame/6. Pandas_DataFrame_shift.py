from pandas import *

s = Series([100, 200, 300])

# shift() 함수는 Series 값을 위나 아래로 밀어내는 함수이다
# 값을 위로 올리고 싶으면 -1
s2 = s.shift(1)

print(s)
print(s2)
