# importing the libraries
import numpy as np
import pandas as pd
import os
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

scale = StandardScaler()
os.chdir(os.path.dirname(os.path.realpath(__file__)))
# loading dataset and storing in train variable
raw_training_dataset = pd.read_csv('../dataset/horly_data_to_be_used.csv')

# Fill the empty value in 
x = raw_training_dataset.iloc[:,1:-1].values
y = raw_training_dataset.iloc[:,-1].values

imputer = SimpleImputer(missing_values=np.nan,strategy='median')
training_dataset = imputer.fit_transform(x) 
# training_dataset = scale.fit_transform(training_dataset)
# print("Scale")

print("No Scale")
x_train, x_test, y_train, y_test = train_test_split(training_dataset,y,test_size=0.2,random_state=42)



