import pandas as pd

df = pd.read_csv("dataset/horly_data_to_be_used.csv")

print(df.isna().sum())

