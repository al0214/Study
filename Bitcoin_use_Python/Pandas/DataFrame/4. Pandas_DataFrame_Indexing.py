import pandas as pd

data = {"open" : [730, 750],
        "High" : [755, 780],
        "Low" : [700, 710],
        "Close" : [750, 770]}
df = pd.DataFrame(data, index=["2018-01-01", "2018-01-02"])
# print(df["open"])

# loc 메서드에 특정 인덱스를 넘겨주면 해당하는 행의 데이터가 Series로 반환됩니다. 
print(df.loc["2018-01-01"])

# iloc 메서드를 사용하면 자동으로 맵핑되는 숫자 index로 값을 얻어올 수 있습니다.
print(df.iloc[0]) 

# 예를 들어 2018-01월의 일봉 데이터가 DataFrame 객체로 저장되어 있을 때 첫 번째 거래일의 일봉 데이터를 얻어와야 하는 경우

# loc 방법
target = ["2018-01-01", "2018-01-02"]
print(df.loc[target])

# iloc 방법
target = [0, 1]
print(df.iloc[target])