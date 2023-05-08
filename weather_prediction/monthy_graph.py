import pandas as pd
import matplotlib.pyplot as plt
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))

df = pd.read_csv("../dataset/monthly_data.csv")

year = 2023

new_df = df.loc[df['year'] == year]

aqi_list = new_df['AQI'].to_list()
ch4_list = new_df['ch4'].to_list()
co_list = new_df['CO'].to_list()
so2_list = new_df['SO2'].to_list()
butane_list = new_df['butane'].to_list()
coal_list = new_df['coal'].to_list()
month = ['January','Febuary','March','April','May','June','July','August','September','October','November','December']

# Comment to generate only gases
# plt.plot(month,aqi_list,c='red',label='AQI')


# Comment to generate only AQI
plt.plot(month,ch4_list,c='BLUE',label='CH4')
plt.plot(month,co_list,c='green',label='Carbon Monoxide')
plt.plot(month,so2_list,c='red',label='Sulphur')
plt.plot(month,coal_list,c='pink',label='CoalGas')
plt.plot(month,butane_list,c='orange',label='Butane')

 
plt.xlabel(f'{year} - Months')
plt.ylabel('PPM')
plt.title("Monthly AQI")
plt.legend()
plt.show()
