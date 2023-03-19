import pandas as pd
import datetime 

df = pd.read_csv("dataset/horly_data_to_be_used.csv")

print(df)
# df['date'] = datetime.datetime.strptime(df['Datetime'],"%d-%m-%Y %H:%M")

# print(df)