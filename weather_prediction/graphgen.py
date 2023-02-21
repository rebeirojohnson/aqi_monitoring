import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("dataset/horly_data_to_be_used.csv")

df2 = df.dropna()

print(df.isna().sum())

plt.scatter(df2['NO2'],df2['AQI'],c='red')

plt.show()
