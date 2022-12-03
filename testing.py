import os
import joblib
from preprocess import x_test,y_test

os.chdir(os.path.dirname(os.path.realpath(__file__)))

random_forest_model = joblib.load('random_forest_model.pkl')
boostreg_model = joblib.load('boostreg_model.pkl')
mlr_model = joblib.load('mlr_model.pkl')
# 667

val1 = random_forest_model.predict([[61.13,0.43,14.07,12.9,0.43,34.47,106.88]])
print(val1)
val = boostreg_model.predict([[61.13,0.43,14.07,12.9,0.43,34.47,106.88]])
print(val)
val1 = mlr_model.predict([[61.13,0.43,14.07,12.9,0.43,34.47,106.88]])
print(val1)
# predicting the output and checking for the r2_score
from sklearn.metrics import r2_score
y_pred = random_forest_model.predict(x_test)
print("randoms")
print(r2_score(y_test,y_pred))

y_pred = boostreg_model.predict(x_test)
print("Bool")
print(r2_score(y_test,y_pred))

y_pred = mlr_model.predict(x_test)
print("mlr")
print(r2_score(y_test,y_pred))
