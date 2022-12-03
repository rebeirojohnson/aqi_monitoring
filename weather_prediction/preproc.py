import pandas as pd
import joblib

df = pd.read_csv("./dataset/city_data.csv")

# pm25_df = df[['Datetime','PM2.5']]
# NO_df = df[['Datetime','NO']]
# NO2_df = df[['Datetime','NO2']]
# NOx_df = df[['Datetime','NOx']]
# CO_df = df[['Datetime','CO']]
# SO2_df = df[['Datetime','SO2']]
# O3_df = df[['Datetime','O3']]

# pm25_df = pm25_df[pm25_df['PM2.5'].notna()]
# NO_df = NO_df[NO_df['NO'].notna()]
# NO2_df = NO2_df[NO2_df['NO2'].notna()]
# NOx_df = NOx_df[NOx_df['NOx'].notna()]
# CO_df = CO_df[CO_df['CO'].notna()]
# SO2_df = SO2_df[SO2_df['SO2'].notna()]
# O3_df = O3_df[O3_df['O3'].notna()]
#  # x is always extracted with range
# NO = NO_df.iloc[:,:-1].values
# NO2 = NO2_df.iloc[:,:-1].values
# NOx = NOx_df.iloc[:,:-1].values
# CO = CO_df.iloc[:,:-1].values
# SO2 = SO2_df.iloc[:,:-1].values
# O3 = O3_df.iloc[:,:-1].values
# AQI = df.iloc[:,-1].values

print(df)
