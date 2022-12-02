import os
import joblib
from preprocess import output_array,training_array,x_test,y_test

os.chdir(os.path.dirname(os.path.realpath(__file__)))

# random_forest_model = joblib.load('random_forest_model.pkl')
# boostreg_model = joblib.load('boostreg_model.pkl')
multi_layer_pre_model = joblib.load('multi_layer_pre_model.pkl')
#mlr_model = joblib.load('mlr_model.pkl').pkl
# 667

# val1 = random_forest_model.predict([[67.57,0.63,15.84,15.12,0.63,27.26,82.96]])
# print(val1)
# r1 = random_forest_model.score(x_test, y_test) * 100
# print(r1)

# val = boostreg_model.predict([[67.57,0.63,15.84,15.12,0.63,27.26,82.96]])
# print(val)
# r2 = boostreg_model.score(x_test, y_test)*100
# print(r2)

# val1 = mlr_model.predict([[67.57,0.63,15.84,15.12,0.63,27.26,82.96]])
# print(val1)

val1 = multi_layer_pre_model.predict([[67.57,0.63,15.84,15.12,0.63,27.26,82.96]])
print(val1)
r1 = multi_layer_pre_model.score(x_test, y_test) * 100
print(r1)
