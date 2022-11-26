# importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from sklearn.impute import SimpleImputer
# importing Randomforest
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor
import joblib

os.chdir(os.path.dirname(os.path.realpath(__file__)))

# loading dataset and storing in train variable
training_dataset = pd.read_csv('dataset/city_data_val_test.csv')
 
# Fill the empty value in 
imputer = SimpleImputer(missing_values=np.nan,strategy='median')
training_dataset = imputer.fit_transform(training_dataset) 


# separating class label and other attributes
training_array = np.delete(training_dataset,obj=9, axis=1)
output_array = training_dataset[:, -1]


# creating model
random_forest_model = RandomForestRegressor()
boostreg_model = AdaBoostRegressor()


# Fitting the model
random_forest_model.fit(training_array, output_array)
boostreg_model.fit(training_array, output_array)

# printing score
r1 = random_forest_model.score(training_array, output_array) * 100
r2 = boostreg_model.score(training_array, output_array)*100


joblib.dump(random_forest_model, 'random_forest_model.pkl')
joblib.dump(boostreg_model, 'boostreg_model.pkl')
