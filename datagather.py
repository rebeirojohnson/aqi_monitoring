import pandas as pd

df = pd.read_csv("dataset/hourly_data.csv")

df2 = df.dropna(thresh=3)

df3 = df2.loc[df2['AQI'].notnull()]

print(df3.isna().sum())

df3 = df3.dropna(thresh=3)

print(df3.isna().sum())

print(df3)

