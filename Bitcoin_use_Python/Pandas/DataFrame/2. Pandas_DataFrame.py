import pandas as pd
from pandas import Series

df = pd.read_excel("/Users/samoyed/Documents/Study/Bitcoin_use_Python/Pandas/DataFrame/ExamExel.xlsx")
df = df.set_index('date')
df = df.to_excel("/Users/samoyed/Documents/Study/Bitcoin_use_Python/Pandas/DataFrame/ExamExel2.xlsx")
print(df)
