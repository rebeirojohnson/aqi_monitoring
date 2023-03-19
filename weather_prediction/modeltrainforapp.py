from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from preproc import *
from sklearn.metrics import r2_score

reg = LinearRegression()

pm25 = pm25_df.iloc[:,:-1].values
y = pm25_df.iloc[:,-1].values
x_train, x_test, y_train, y_test = train_test_split(pm25,y,test_size=0.2,random_state= 0)
reg.fit(X= x_train,y = y_train)
joblib.dump(reg, 'pkl_file/pm25.pkl')

y = NO_df.iloc[:,-1].values
x_train, x_test, y_train, y_test = train_test_split(NO,y,test_size=0.2,random_state= 0)
reg.fit(X= x_train,y = y_train)
joblib.dump(reg, 'pkl_file/no.pkl')


y = NO2_df.iloc[:,-1].values
x_train, x_test, y_train, y_test = train_test_split(NO2,y,test_size=0.2,random_state= 0)
reg.fit(X= x_train,y = y_train)
joblib.dump(reg, 'pkl_file/no2.pkl')

y = NOx_df.iloc[:,-1].values
x_train, x_test, y_train, y_test = train_test_split(NOx,y,test_size=0.2,random_state= 0)
reg.fit(X= x_train,y = y_train)
joblib.dump(reg, 'pkl_file/nox.pkl')

y = Nh3_df.iloc[:,-1].values
x_train, x_test, y_train, y_test = train_test_split(Nh3,y,test_size=0.2,random_state= 0)
reg.fit(X= x_train,y = y_train)
joblib.dump(reg, 'pkl_file/nh3.pkl')


y = CO_df.iloc[:,-1].values
x_train, x_test, y_train, y_test = train_test_split(CO,y,test_size=0.2,random_state= 0)
reg.fit(X= x_train,y = y_train)
joblib.dump(reg, 'pkl_file/co.pkl')

y = SO2_df.iloc[:,-1].values
x_train, x_test, y_train, y_test = train_test_split(SO2,y,test_size=0.2,random_state= 0)
reg.fit(X= x_train,y = y_train)
joblib.dump(reg, 'pkl_file/so2.pkl')


y = O3_df.iloc[:,-1].values
x_train, x_test, y_train, y_test = train_test_split(O3,y,test_size=0.2,random_state= 0)
reg.fit(X= x_train,y = y_train)
joblib.dump(reg, 'pkl_file/o3.pkl')



