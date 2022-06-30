from pandas import DataFrame, Series

data = {"open" : [730, 750],
        "High" : [755, 780],
        "Low" : [700, 710],
        "Close" : [750, 770]}
df = DataFrame(data)

s = Series([300, 400])
df['Volume'] = s
# = 위치가 중요

print(df)

# loc로 추가
df.loc[2] = (100, 200, 300, 400, 500) # 데이터의 개수가 DataFrame 행의 데이터 개수와 동일해야 함에 주의
print(df)

# 기존 데이터를 응용하여 추가하기
upper = df["open"] * 1.3
df["upper"] = upper
print(df)