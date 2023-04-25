import os
import joblib
from preprocess import x_test,y_test
from matplotlib import pyplot as plt
import numpy as np
from sklearn.metrics import r2_score,accuracy_score



os.chdir(os.path.dirname(os.path.realpath(__file__)))

random_forest_model = joblib.load('../pkl_file/random_forest_model.pkl')
mlr_model = joblib.load('../pkl_file/mlr_model.pkl')
svmrbf_model = joblib.load('../pkl_file/svmrbf.pkl')
svmlin_model = joblib.load('../pkl_file/svmlin.pkl')
lasso_model = joblib.load('../pkl_file/lasso_model.pkl')
ridge_model = joblib.load('../pkl_file/ridge_model.pkl')

start,stop = 0,10
model_name = "Random Forest"
y_pred = random_forest_model.predict(x_test[start:stop])
print(f"Accuracy of {model_name} is {round(r2_score(y_test[start:stop],y_pred)*100,3)}%")
plt.scatter(x_test[start:stop,1],y_test[start:stop],c='red',label='original test values')
plt.scatter(x_test[start:stop,1],y_pred,c='blue',label='predicted  values')
plt.xlabel('PM2.5')
plt.ylabel('AQI')
plt.title("Random Forest")
plt.legend()
plt.show()

start,stop = 0,10
model_name = "Multi Linear regression"
y_pred = mlr_model.predict(x_test[start:stop])
print(f"Accuracy of {model_name} is {round(r2_score(y_test[start:stop],y_pred)*100,3)}%")
plt.scatter(x_test[start:stop,1],y_test[start:stop],c='red',label='original test values')
plt.scatter(x_test[start:stop,1],y_pred,c='blue',label='predicted  values')
plt.xlabel('PM2.5')
plt.ylabel('AQI')
plt.title("Multi Linear")
plt.legend()
plt.show()

start,stop = 0,10
model_name = "SVR"
y_pred = svmrbf_model.predict(x_test[start:stop])
print(f"Accuracy of {model_name} is {round(r2_score(y_test[start:stop],y_pred)*100,3)}%")
plt.scatter(x_test[start:stop,1],y_test[start:stop],c='red',label='original test values')
plt.scatter(x_test[start:stop,1],y_pred,c='blue',label='predicted  values')
plt.xlabel('PM2.5')
plt.ylabel('AQI')
plt.title("svmrbf_model")
plt.legend()
plt.show()

start,stop = 0,10
y_pred = svmlin_model.predict(x_test[start:stop])
model_name = "Linear SVR"
print(f"Accuracy of {model_name} is {round(r2_score(y_test[start:stop],y_pred)*100,3)}%")
plt.scatter(x_test[start:stop,1],y_test[start:stop],c='red',label='original test values')
plt.scatter(x_test[start:stop,1],y_pred,c='blue',label='predicted  values')
plt.xlabel('PM2.5')
plt.ylabel('AQI')
plt.title("SVR Linear")
plt.legend()
plt.show()

start,stop = 0,10
model_name = "Lasso Forest"
y_pred = lasso_model.predict(x_test[start:stop])
print(f"Accuracy of {model_name} is {round(r2_score(y_test[start:stop],y_pred)*100,3)}%")
plt.scatter(x_test[start:stop,1],y_test[start:stop],c='red',label='original test values')
plt.scatter(x_test[start:stop,1],y_pred,c='blue',label='predicted  values')
plt.xlabel('PM2.5')
plt.ylabel('AQI')
plt.title("lasso Model")
plt.legend()
plt.show()

start,stop = 0,10
model_name = "Ridge Model"
y_pred = ridge_model.predict(x_test[start:stop])
print(f"Accuracy of {model_name} is {round(r2_score(y_test[start:stop],y_pred)*100,3)}%")
plt.scatter(x_test[start:stop,1],y_test[start:stop],c='red',label='original test values')
plt.scatter(x_test[start:stop,1],y_pred,c='blue',label='predicted  values')
plt.xlabel('PM2.5')
plt.ylabel('AQI')
plt.title("ridge_model")
plt.legend()
plt.show()



