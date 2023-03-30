# importing the libraries
import os
from preprocess import x_train, x_test, y_train, y_test
# importing Randomforest
from sklearn.linear_model import LinearRegression,Lasso,Ridge
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVR # "Support vector classifier"  

import joblib

os.chdir(os.path.dirname(os.path.realpath(__file__)))

# creating model
boostreg_model = AdaBoostRegressor()
multi_layer_pre_model = MLPClassifier(random_state=1, max_iter=200)
knn5 = KNeighborsClassifier(n_neighbors = 5)
knn1 = KNeighborsClassifier(n_neighbors=1)
mlr_model = LinearRegression()
svr_rbf = SVR(kernel="rbf", C=100, gamma=0.1, epsilon=0.1)
svr_lin = SVR(kernel="linear", C=100, gamma="auto")
svr_poly = SVR(kernel="poly", C=100, gamma="auto", degree=3, epsilon=0.1, coef0=1)

random_forest_model = RandomForestRegressor(n_estimators=39, random_state=0)
lasso_model = Lasso(alpha=0.1)
ridge_model = Ridge(alpha=1)

# Fitting the model
from sklearn.metrics import accuracy_score

print("Random forest started")
random_forest_model.fit(x_train, y_train)
joblib.dump(random_forest_model, '../pkl_file/random_forest_model.pkl')
print("Random forest finished")

# print("boostreg started")
# boostreg_model.fit(x_train,y_train)
# joblib.dump(boostreg_model,'../pkl_file/boostreg_model.pkl')
# print("boostreg finished")

# # print("mepc started")
# # multi_layer_pre_model.fit(x_train,y_train)
# # joblib.dump(multi_layer_pre_model,'../pkl_file/multi_layer_pre_model.pkl')
# # print("mrpc finish")

# print("mlr model started")
# mlr_model.fit(x_train, y_train)
# joblib.dump(mlr_model, '../pkl_file/mlr_model.pkl')
# print("mlr model finished")

# print("knn1 started")
# knn1.fit(x_train, y_train)
# joblib.dump(knn1, '../pkl_file/knn1.pkl')
# print("knn1 finished")

# print("knn5 started")
# knn5.fit(x_train, y_train)
# joblib.dump(knn5, '../pkl_file/knn5.pkl')
# print("knn5 finished")

# print("SVR started")
# svr_rbf.fit(x_train, y_train)  
# joblib.dump(svr_rbf, '../pkl_file/svmrbf.pkl')
# print("SVM finished")

# print("SVR started")
# svr_lin.fit(x_train, y_train)  
# joblib.dump(svr_rbf, '../pkl_file/svmlin.pkl')
# print("SVM finished")

# print("Lasso started")
# lasso_model.fit(x_train, y_train)  
# joblib.dump(lasso_model, '../pkl_file/lasso_model.pkl')
# print("laso finished")

# print("Ridge started")
# ridge_model.fit(x_train, y_train)  
# joblib.dump(ridge_model, '../pkl_file/ridge_model.pkl')
# print("ridge_model finished")

# # print("Poly started")
# # svr_poly.fit(x_train, y_train)  
# # joblib.dump(svr_rbf, '../pkl_file/svmpoly.pkl')
# # print("SVM finished")


