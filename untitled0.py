# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LLlgYaljZsdOzl3NBqyuau4fOySpfdAy
"""

from google.colab import drive
drive.mount('/content/gdrive')
path_to_csv = '/content/data (1).csv'
import warnings
warnings.filterwarnings("ignore")

import pandas as pd
# Read the provided CSV file ‘data.csv’
df = pd.read_csv(path_to_csv)
df

# Show the basic statistical description about the data.
df.describe()

# Check if the data has null values.
print('Are there any null values: ',df.isnull().values.any())
# Replace the null values with the mean
df.fillna(df.mean(),inplace=True)
print('Are there any null values after using fillna: ',df.isnull().values.any())

# Select at least two columns and aggregate the data using: min, max, count, mean.
aggre = df.groupby('Duration').agg({'Calories':['mean','min','max','count']})
aggre

# Filter the dataframe to select the rows with calories values between 500 and 1000
df[(df['Calories']>=500) & (df['Calories']<=1000)]

# Filter the dataframe to select the rows with calories values > 500 and pulse < 100
df[(df['Calories']>500) & (df['Pulse']<100)]

# Create a new “df_modified” dataframe that contains all the columns from df except for “Maxpulse”
df_modified = df[['Duration', 'Pulse', 'Calories']]
df_modified

# Delete the “Maxpulse” column from the main df dataframe
df = df.drop('Maxpulse', axis=1)
df

# Convert the datatype of Calories column to int datatype
df['Calories'] = df['Calories'].astype('int64')
df.dtypes

# Using pandas create a scatter plot for the two columns (Duration and Calories)
df.plot.scatter(x='Duration', y='Calories')

glass=pd.read_csv("/content/glass.csv")
	glass.head()
	des=glass.corr()
	glass.corr().style.background_gradient(cmap="Greens")

import warnings
from sklearn.model_selection import train_test_split, cross_validate
features = ['Rl', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe']
target = 'Type'


X_train, X_val, Y_train, Y_val = train_test_split(glass[::-1], glass[target],test_size=0.2, random_state=1)

import warnings
from sklearn.metrics import accuracy_score, recall_score, precision_score, classification_report, confusion_matrix
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()

classifier.fit(X_train, Y_train)

y_pred = classifier.predict(X_val)

# Summary of the predictions made by the classifier
print(classification_report(Y_val, y_pred))
print(confusion_matrix(Y_val, y_pred))
# Accuracy score
from sklearn.metrics import accuracy_score
print('\naccuracy is',accuracy_score(Y_val, y_pred))

from sklearn.svm import SVC, LinearSVC
classifier = LinearSVC()

classifier.fit(X_train, Y_train)

y_pred = classifier.predict(X_val)

# Summary of the predictions made by the classifier
print(classification_report(Y_val, y_pred))
print(confusion_matrix(Y_val, y_pred))
# Accuracy score
from sklearn.metrics import accuracy_score
print('\naccuracy is',accuracy_score(Y_val, y_pred))



import seaborn as sns

sns.heatmap(data=glass) #HeatMap Visualization for above dataset

sns.scatterplot(data=glass)  #ScatterPlot Visualization for above dataset