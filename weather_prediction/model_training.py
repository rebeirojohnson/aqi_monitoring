# importing the libraries
import os
from preprocess import x_train, x_test, y_train, y_test
# importing Randomforest
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC # "Support vector classifier"  

import joblib

os.chdir(os.path.dirname(os.path.realpath(__file__)))

# creating model
random_forest_model = RandomForestRegressor(n_estimators=9, random_state=0)
boostreg_model = AdaBoostRegressor()
multi_layer_pre_model = MLPClassifier(random_state=1, max_iter=300)
knn5 = KNeighborsClassifier(n_neighbors = 5)
knn1 = KNeighborsClassifier(n_neighbors=1)
mlr_model = LinearRegression()
svm = SVC(kernel='rbf', random_state=0)  


print(x_train)
# Fitting the model
from sklearn.metrics import accuracy_score

print("Random forest started")
random_forest_model.fit(x_train, y_train)
joblib.dump(random_forest_model, '../pkl_file/random_forest_model.pkl')
print("Random forest finished")

print("boostreg started")
boostreg_model.fit(x_train,y_train)
joblib.dump(boostreg_model,'../pkl_file/boostreg_model.pkl')
print("boostreg finished")

# print("mepc started")
# multi_layer_pre_model.fit(x_train,y_train)
# joblib.dump(multi_layer_pre_model,'../pkl_file/multi_layer_pre_model.pkl')
# print("mrpc finish")

print("mlr model started")
mlr_model.fit(x_train, y_train)
joblib.dump(mlr_model, '../pkl_file/mlr_model.pkl')
print("mlr model finished")

print("knn1 started")
knn1.fit(x_train, y_train)
joblib.dump(knn1, '../pkl_file/knn1.pkl')
print("knn1 finished")

print("knn5 started")
knn5.fit(x_train, y_train)
joblib.dump(knn5, '../pkl_file/knn5.pkl')
print("knn5 finished")

print("SVM started")
svm.fit(x_train, y_train)  
joblib.dump(svm, '../pkl_file/svm.pkl')
print("SVM finished")

