import pandas as pd

df = pd.read_csv("dataset/horly_data_to_be_used.csv")

df2 = df.dropna(thresh=3)

print(df2.isna().sum())

df2 = df2.dropna(thresh=7)

df.to_csv("dataset/horly_data_to_be_used.csv")


