import pandas as pd

df = pd.read_csv("DB.csv")
# print(df.iloc[-1]['id'])
print(df.iloc[2:301])
