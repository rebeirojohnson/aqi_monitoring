import os
import joblib
from preprocess import x_test,y_test
from matplotlib import pyplot as plt
import numpy as np
from sklearn.metrics import r2_score,accuracy_score
x_test,y_test = x_test[:20],y_test[0:20]



os.chdir(os.path.dirname(os.path.realpath(__file__)))

random_forest_model = joblib.load('../pkl_file/random_forest_model.pkl')
mlr_model = joblib.load('../pkl_file/mlr_model.pkl')
svmrbf_model = joblib.load('../pkl_file/svmrbf.pkl')
svmlin_model = joblib.load('../pkl_file/svmlin.pkl')
lasso_model = joblib.load('../pkl_file/lasso_model.pkl')
ridge_model = joblib.load('../pkl_file/ridge_model.pkl')

models = [random_forest_model,mlr_model,svmlin_model,svmrbf_model,lasso_model,ridge_model]

for model in models:
    y_pred = model.predict(x_test)
    print(str(model))
    print("Accuracy ",r2_score(y_test,y_pred))
    # plt.scatter(x_test[:,1],y_test,c='red',label='original test values')
    # plt.scatter(x_test[:,1],y_pred,c='blue',label='predicted  values')
    print(np.append(arr=y_test.reshape(len(y_test),1),values=y_pred.reshape(len(y_pred),1),axis=1))
    # plt.xlabel('PM2.5')d
    # plt.ylabel('AQI')
    # plt.title(str(model))
    # plt.legend()
    # plt.show()



