'''
Add various model
k nearest neighbour
support vector regression
multilinear regression
gaussian air dispersion model
logistic regression
naive bayes
'''

import pandas as pd
raw_training_dataset = pd.read_csv('dataset/city_data_val.csv')
print(raw_training_dataset.isna().sum())

print(len(raw_training_dataset))