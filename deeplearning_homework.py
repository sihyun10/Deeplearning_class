# -*- coding: utf-8 -*-
"""deeplearning_homework.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ivlC4ElDCIafMsbHSbdd4adBJ-7gsZ5p
"""

import math
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import KFold
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, mean_absolute_error

def mean_absolute_percentage_error(y_true, y_pred):
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

data = pd.read_csv("/content/Assignment Material.csv", engine='python')
data.head()

train_data= data.iloc[7:729, 4:29]# 2009년부터2010년까지

test_data= data.iloc[729:, 4:29]# 2011년

#데이터 정규화 수행하기

X_Data= train_data.iloc[:, :-1]
scaler = StandardScaler().fit(X_Data)
X_Data= scaler.transform(X_Data)
Y_Data= train_data.iloc[:, -1]

X_Test= test_data.iloc[:, :-1]
X_Test= scaler.transform(X_Test)
Y_Test= test_data.iloc[:, -1]

model = MLPRegressor(hidden_layer_sizes=(13,13,13,13,13), activation='relu', 
                     solver='adam', alpha=0.0001, batch_size=18, learning_rate='constant', 
                     learning_rate_init=0.001, power_t=0.5, max_iter=150, random_state=42)

model.fit(X_Data, Y_Data.values.ravel())
Y_Pred= model.predict(X_Test)
Y_True= Y_Test

rmse= math.sqrt(mean_squared_error(Y_Pred, Y_True))
mae= mean_absolute_error(Y_Pred, Y_True)
mape= mean_absolute_percentage_error(Y_True, Y_Pred)

Y_Pred= pd.DataFrame(Y_Pred, columns=["Prediction"])
Y_Pred.to_csv("ANN1.csv", header=True, index=False)

result = []
result.append(["HL=1", rmse, mae, mape])

result