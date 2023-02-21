import os
import joblib
from preprocess import x_test,y_test
from matplotlib import pyplot as plt
import numpy as np

os.chdir(os.path.dirname(os.path.realpath(__file__)))

random_forest_model = joblib.load('../pkl_file/random_forest_model.pkl')
boostreg_model = joblib.load('../pkl_file/boostreg_model.pkl')
mlr_model = joblib.load('../pkl_file/mlr_model.pkl')
mpec_model = joblib.load('../pkl_file/multi_layer_pre_model.pkl')
knn1_model = joblib.load('../pkl_file/knn1.pkl')
knn5_model = joblib.load('../pkl_file/knn5.pkl')
svmrbf_model = joblib.load('../pkl_file/svmrbf.pkl')
svmlin_model = joblib.load('../pkl_file/svmlin.pkl')
lasso_model = joblib.load('../pkl_file/lasso_model.pkl')
ridge_model = joblib.load('../pkl_file/ridge_model.pkl')
# svmpoly_model = joblib.load('../pkl_file/svmpoly.pkl')

#265
# val1 = random_forest_model.predict([[15.01,1.74,23.51,13.12,8.7,3,1.67,5.12]])
# print(val1)
# val = boostreg_model.predict([[45.26,2.62,20.09,14.04,19.67,29.04,1.1,25.26]])
# print(val)
# val1 = mlr_model.predict([[45.26,2.62,20.09,14.04,19.67,29.04,1.1,25.26]])
# print(val1)
# val1 = mpec_model.predict([[45.26,2.62,20.09,14.04,19.67,29.04,1.1,25.26]])
# print(val1)
# val1 = knn1_model.predict([[45.26,2.62,20.09,14.04,19.67,29.04,1.1,25.26]])
# print(val1)
# val1 = knn5_model.predict([[45.26,2.62,20.09,14.04,19.67,29.04,1.1,25.26]])
# print(val1)

# predicting the output and checking for the r2_score
from sklearn.metrics import r2_score,accuracy_score

# y_pred = random_forest_model.predict(x_test)
# print("randoms")
# print(r2_score(y_test,y_pred))

# y_pred = boostreg_model.predict(x_test)
# print("Bool")
# print(r2_score(y_test,y_pred))

# y_pred = mlr_model.predict(x_test)
# print("mlr")
# print(r2_score(y_test,y_pred))

# y_pred = mpec_model.predict(x_test)
# print("Mpec")
# print(r2_score(y_test,y_pred))
# print(accuracy_score(y_test,y_pred)*100)

# y_pred = knn1_model.predict(x_test)
# print("Knn1")
# print(r2_score(y_test,y_pred))
# print(accuracy_score(y_test,y_pred)*100)


# y_pred = knn5_model.predict(x_test)
# # print(y_pred)
# # print(y_test)
# print("Knn5")
# print(r2_score(y_test,y_pred))
# print("Knn5")
# print(accuracy_score(y_test,y_pred)*100)
# print('y_test               y_pred')
# plt.plot(x_test[:,1],y_test,c='red',label='original test values')
# plt.scatter(x_test[:,1],y_pred,c='blue',label='predicted  values')
# plt.xlabel('Admin')
# plt.ylabel('AQI')
# plt.legend()
# plt.show()
# print(np.append(arr=y_test.reshape(len(y_test),1),
#                 values=y_pred.reshape(len(y_pred),1),axis=1))

# y_pred = svmrbf_model.predict(x_test)
# print("Svmrbf")
# print(r2_score(y_test,y_pred))

# # y_pred = svmpoly_model.predict(x_test)
# # print("Svmpoly")
# # print(r2_score(y_test,y_pred))

# y_pred = svmlin_model.predict(x_test)
# print("Svmliin")
# print(r2_score(y_test,y_pred))

y_pred = lasso_model.predict(x_test)
print("Lasso")
print(r2_score(y_test,y_pred))

y_pred = ridge_model.predict(x_test)
print("Ridge")
print(r2_score(y_test,y_pred))




