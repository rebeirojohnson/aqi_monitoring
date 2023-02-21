import pandas as pd

df = pd.read_csv("dataset/horly_data_to_be_used.csv")

print(df.isna().sum())

df2 = df.dropna(thresh=7)

print(df2.isna().sum())
