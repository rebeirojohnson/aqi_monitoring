import os
import joblib

os.chdir(os.path.dirname(os.path.realpath(__file__)))

random_forest_model = joblib.load('random_forest_model.pkl')
boostreg_model = joblib.load('boostreg_model.pkl')
mlr_model = joblib.load('mlr_model.pkl')
# 667

val1 = random_forest_model.predict([[11.38,0, 2.62,12.13,12.22, 0,2.62,47.12,97.5,125.25,101.72]])
print(val1)
val = boostreg_model.predict([[11.38,0, 2.62,12.13,12.22, 0,2.62,47.12,97.5,125.25,101.72]])
print(val)
val1 = mlr_model.predict([[11.38,0, 2.62,12.13,12.22, 0,2.62,47.12,97.5,125.25,101.72]])
print(val1)
