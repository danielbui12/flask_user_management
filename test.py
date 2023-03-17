import pandas as pd

df = pd.read_csv("DB.csv")
df = df.fillna(method = 'ffill')
print(df[df["price"]>0] )
df.to_csv("DB.csv", index=False)
# # print(df.iloc[-1]['id'])
# print(df.iloc[2:301])


from urllib.parse import quote, unquote
s = "{ 'key': 'id', 'value': 'ascending' }"
encoded_s = quote(s) # 'Hello%20world%21'
print(encoded_s)

decoded_s = unquote(s) # 'Hello world!'
print(decoded_s)

