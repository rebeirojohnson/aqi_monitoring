import pandas as pd
import joblib
import datetime

df = pd.read_csv("dataset/horly_data_to_be_used.csv")

for index,row in df.iterrows():
    dateobj = datetime.datetime.strptime(row['Datetime'],"%d-%m-%Y %H:%M")
    df.loc[index, ['Datetime']] = [int(datetime.datetime.strftime(dateobj,"%Y%m%d"))]


pm25_df = df[['Datetime','PM2.5']]
NO_df = df[['Datetime','NO']]
NO2_df = df[['Datetime','NO2']]
NOx_df = df[['Datetime','NOx']]
Nh3_df = df[['Datetime','NH3']]
CO_df = df[['Datetime','CO']]
SO2_df = df[['Datetime','SO2']]
O3_df = df[['Datetime','O3']]

pm25_df = pm25_df[pm25_df['PM2.5'].notna()]
NO_df = NO_df[NO_df['NO'].notna()]
NO2_df = NO2_df[NO2_df['NO2'].notna()]
NOx_df = NOx_df[NOx_df['NOx'].notna()]
Nh3_df = Nh3_df[Nh3_df['NH3'].notna()]
CO_df = CO_df[CO_df['CO'].notna()]
SO2_df = SO2_df[SO2_df['SO2'].notna()]
O3_df = O3_df[O3_df['O3'].notna()]
 # x is always extracted with range
NO = NO_df.iloc[:,:-1].values
NO2 = NO2_df.iloc[:,:-1].values
NOx = NOx_df.iloc[:,:-1].values
Nh3 = Nh3_df.iloc[:,:-1].values
CO = CO_df.iloc[:,:-1].values
SO2 = SO2_df.iloc[:,:-1].values
O3 = O3_df.iloc[:,:-1].values
AQI = df.iloc[:,-1].values


