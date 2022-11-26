import os
import joblib

os.chdir(os.path.dirname(os.path.realpath(__file__)))

models = ["random_forest_model","boostreg_model"]

random_forest_model = joblib.load('random_forest_model.pkl')
boostreg_model = joblib.load('boostreg_model.pkl')

val1 = random_forest_model.predict([[93.57,4.17,41.95,49.48,4.17,110.68,11.5,0.47,0]])
print(val1)
val = boostreg_model.predict([[93.57,4.17,41.95	,49.48,4.17	,110.68,11.5,0.47,0]])
print(val)
