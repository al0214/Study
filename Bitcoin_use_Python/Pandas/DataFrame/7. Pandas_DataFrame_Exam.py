from matplotlib.pyplot import axis
from pandas import *

data = {"open" : [737, 750, 770],
        "High" : [755, 780, 770],
        "Low" : [700, 710, 750],
        "Close" : [750, 770, 730]}
df = DataFrame(data, index=["2018-01-01", "2018-01-02", "2018-01-03"])
print(df)

s = Series([55, 70, 20], index=["2018-01-01", "2018-01-02", "2018-01-03"])
df["volatility"] = s
print(df)
