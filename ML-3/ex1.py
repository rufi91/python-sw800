"""
Develop an ML model for predicting sales for the Advertising data
(Advertising.csv file) using Linear Regression.
"""

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv('/home/ai21/Desktop/common/ML/Day3/Advertising.csv')
data=data.as_matrix()
X = data[:,1:3]
y = data[:,-1]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print X_train.size
print y_train.size

lr=LinearRegression()
lr.fit(X_train, y_train)
p=lr.predict(X_test)

print "=============Predictions==============\n\n", p
plt.scatter(y_test,p)
plt.show()
