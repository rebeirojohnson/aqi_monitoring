import pandas as pd
import matplotlib.pyplot as plt
import os
from statistics import mean
import numpy as np
from sklearn.impute import SimpleImputer

os.chdir(os.path.dirname(os.path.realpath(__file__)))

df = pd.read_csv("../dataset/city_day3.csv")

imputer = SimpleImputer(missing_values=np.nan,strategy='median')
df = imputer.fit_transform(df) 

outdf = pd.DataFrame(columns=['Month','ch4','coal','butane','NOx','NH3','CO','SO2','O3','AQI','year'])

for years in [2015,2016,2017,2018,2019,2020]:
    for month in ['01','02','03','04','05','06','07','08','09','10','11','12']:
        mini_df = df.loc[df['Date'].str.contains(f"{month}-{years}") == True]
        no_of_data = mini_df.shape[0]
        if no_of_data != 0:
            pm25avg = sum(mini_df['PM2.5'].to_list())/no_of_data
            print(mini_df['PM2.5'].to_list())
            outdf.loc[outdf.shape[0]] = [month,pm25avg,'coal','butane','NOx','NH3','CO','SO2','O3','AQI',years]
        else:
            outdf.loc[outdf.shape[0]] = [month,0,'coal','butane','NOx','NH3','CO','SO2','O3','AQI',years]
        outdf.to_csv("../dataset/city_data2.csv")

# year = 2023

# new_df = df.loc[df['year'] == year]

# aqi_list = new_df['AQI'].to_list()
# ch4_list = new_df['ch4'].to_list()
# co_list = new_df['CO'].to_list()
# so2_list = new_df['SO2'].to_list()
# butane_list = new_df['butane'].to_list()
# coal_list = new_df['coal'].to_list()
# month = ['January','Febuary','March','April','May','June','July','August','September','October','November','December']

# # Comment to generate only gases
# # plt.plot(month,aqi_list,c='red',label='AQI')


# # Comment to generate only AQI
# plt.plot(month,ch4_list,c='BLUE',label='CH4')
# plt.plot(month,co_list,c='green',label='Carbon Monoxide')
# plt.plot(month,so2_list,c='red',label='Sulphur')
# plt.plot(month,coal_list,c='pink',label='CoalGas')
# plt.plot(month,butane_list,c='orange',label='Butane')

 
# plt.xlabel(f'{year} - Months')
# plt.ylabel('PPM')
# plt.title("Monthly AQI")
# plt.legend()
# plt.show()
