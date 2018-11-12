"""
Develop an ML model to predict the average parking rates per month for a city
from the city related data (city.csv)
"""


from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, mean_squared_error
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data=pd.read_csv('/home/ai21/Desktop/common/ML/Day3/Questions/city.csv')
print data.shape
data=data.as_matrix()

X = data[:,1:4]
y = data[:,5]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print X_train.shape
print y_train.shape

lr=LinearRegression()
lr.fit(X_train, y_train)
p=lr.predict(X_test)

print "=============Predictions==============\n\n", p

plt.scatter(y_test,p)
plt.show()

print "=============Mean Squared Error==============\n\n",mean_squared_error(y_test,p)
print "=============RMSE==============\n\n", np.sqrt(mean_squared_error(y_test,p))

