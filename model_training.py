# importing the libraries
import matplotlib.pyplot as plt
import os
from preprocess import training_array, output_array, x_train, x_test, y_train, y_test,training_dataset
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
# .fit(training_df,output_df)
random_forest_model.fit(training_array, output_array)
boostreg_model.fit(training_array, output_array)
multi_layer_pre_model.fit(training_array, output_array)
knn5.fit(x_train, y_train)
knn1.fit(x_train, y_train)

y_pred_5 = knn5.predict(x_test)
y_pred_1 = knn1.predict(x_test)

from sklearn.metrics import accuracy_score
print("Accuracy with k=5", accuracy_score(y_test, y_pred_5)*100)
print("Accuracy with k=1", accuracy_score(y_test, y_pred_1)*100)


value = multi_layer_pre_model.predict([[93.57,4.17,41.95,49.48,4.17,110.68,11.5,0.47,0]])
print(value)
# printing score
r1 = random_forest_model.score(training_array, output_array) * 100
r2 = boostreg_model.score(training_array, output_array)*100
# r3 = multi_layer_pre_model.score(training_array, output_array)*100

# joblib.dump(random_forest_model, 'random_forest_model.pkl')
joblib.dump(mlr_model, 'mlr_model.pkl')
# joblib.dump(boostreg_model, 'boostreg_model.pkl')
# joblib.dump(multi_layer_pre_model, 'multi_layer_pre_model.pkl')
# joblib.dump(knn1, 'knn1.pkl')
# joblib.dump(knn5, 'knn5.pkl')

