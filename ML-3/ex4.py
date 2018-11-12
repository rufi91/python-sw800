"""

Apply Linear Regression on any suitable dataset from this
(https://people.sc.fsu.edu/~jburkardt/datasets/regression/regression.html)
link
Split the data as train and test sets before developing the model. Plot the actual
and predicted points for test data. Obtain mean squared error & RMSE value

"""

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, mean_squared_error
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data=pd.read_csv('/home/ai21/Ex-Rufza/ML-3/fish.txt', delimiter="  ")
print data.head
data=data.as_matrix()
print data.shape

X = data[:,1:2]
y = data[:,3]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print X_train.size
print y_train.size

lr=LinearRegression()
lr.fit(X_train, y_train)
p=lr.predict(X_test)

print "=============Predictions==============\n\n", p

plt.scatter(y_test,p)
plt.show()

print "=============Mean Squared Error==============\n\n",mean_squared_error(y_test,p)
print "=============RMSE==============\n\n", np.sqrt(mean_squared_error(y_test,p))
