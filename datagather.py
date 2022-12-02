import pandas as pd

df = pd.read_csv("dataset/city_data_val.csv")

print(df)

df2 = df.dropna(thresh=3)
print("###########################################")
print(df2.to_csv("dataset/filtered_city_data_val.csv"))

print(df2.isna().sum())