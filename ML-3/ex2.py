"""
Develop an ML model for predicting home prices
"""


from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np

data=pd.read_csv('/home/ai21/Desktop/common/ML/Day3/loan.csv')
data=data.as_matrix()
X = data[:,0:1]
y = data[:,2]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print X_train.size
print y_train.size

lr=LinearRegression()
lr.fit(X_train, y_train)
p=lr.predict(X_test)

print p
