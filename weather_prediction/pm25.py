from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from preproc import pm25_df
from sklearn.metrics import r2_score

x = pm25_df.iloc[:,:-1].values
y = pm25_df.iloc[:,-1].values

print(x,y)
reg = LinearRegression()

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state= 0)

reg.fit(X= x_train,y = y_train)

y_pred = reg.predict(x_test)
print(r2_score(y_pred=y_pred,y_true=y_test))

val = reg.predict([[1,2,7]]) #63.43
print(val)





