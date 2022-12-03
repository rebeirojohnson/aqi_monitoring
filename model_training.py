# importing the libraries
import matplotlib.pyplot as plt
import os
from preprocess import x_train, x_test, y_train, y_test
# importing Randomforest
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor
from sklearn.neural_network import MLPClassifier
import joblib

os.chdir(os.path.dirname(os.path.realpath(__file__)))

# creating model
random_forest_model = RandomForestRegressor()
boostreg_model = AdaBoostRegressor()
multi_layer_pre_model = MLPClassifier(random_state=1, max_iter=300)
knn5 = KNeighborsClassifier(n_neighbors = 5)
knn1 = KNeighborsClassifier(n_neighbors=1)
mlr_model = LinearRegression()

# Fitting the model
from sklearn.metrics import accuracy_score

# print("Random forest started")
# random_forest_model.fit(x_train, y_train)
# joblib.dump(random_forest_model, 'random_forest_model.pkl')
# print("Random forest finished")

# print("boostreg started")
# boostreg_model.fit(x_train,y_train)
# joblib.dump(boostreg_model, 'boostreg_model.pkl')
# print("boostreg finished")

""" 
print("mepc started")
multi_layer_pre_model.fit(x_train,y_train)
joblib.dump(multi_layer_pre_model,'multi_layer_pre_model.pkl')
print("mrpc finish")
"""
print("mlr model started")
mlr_model.fit(x_train, y_train)
joblib.dump(mlr_model, 'mlr_model.pkl')
print("mlr model finished")

print("knn1 started")
knn1.fit(x_train, y_train)
joblib.dump(knn1, 'knn1.pkl')
print("knn1 finished")

print("knn5 started")
knn5.fit(x_train, y_train)
joblib.dump(knn5, 'knn5.pkl')
print("knn5 finished")


y_pred_1 = knn1.predict(x_test)
y_pred_5 = knn5.predict(x_test)

print("Accuracy with k=5", accuracy_score(y_test, y_pred_5)*100)
print("Accuracy with k=1", accuracy_score(y_test, y_pred_1)*100)
"""
"""