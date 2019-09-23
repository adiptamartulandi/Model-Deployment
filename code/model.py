# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 09:48:45 2019

@author: msi
"""

#importing the libraries
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import recall_score, f1_score, accuracy_score, precision_score
import pickle

#importing the dataset
df = pd.read_csv('training.csv')
df.drop(columns=['ID'], inplace=True)
x = df.drop(columns=['TARGET'])
y = df['TARGET']

#Train test solit the data
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=4)

#Training the data
randomf = RandomForestClassifier()
randomf.fit(x_train, y_train)

#Predicting
y_pred = randomf.predict(x_test)

#Metrics to test the accuracy
a = accuracy_score(y_test, y_pred)
p = precision_score(y_test, y_pred, average='macro')
f = f1_score(y_test, y_pred, average='macro')
r = recall_score(y_test, y_pred, average='macro')

#export pickle
pickle.dump(randomf, open('random_forest_model.pkl', 'wb'))

#loading model from pirckle
model = pickle.load(open('random_forest_model.pkl','rb'))

#load data to predict
df_test = pd.read_csv('testing.csv', delimiter=';')
df_test.drop(columns=['ID'], inplace=True)

#predict
print('--------------------Hasil Prediksi--------------------')
print(model.predict(df_test.iloc[0].values.reshape(1,-1)))
print('--------------------Nilai Akurasi--------------------')
print(a)
print('--------------------Nilai Presisi--------------------')
print(p)
print('--------------------Nilai F1-Score--------------------')
print(f)
print('--------------------Nilai Recall--------------------')
print(r)
