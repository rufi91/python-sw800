"""
1) Suppose you are the CEO of a restaurant franchise and are considering
different cities for opening a new outlet. The chain already has outlets in
various cities and you have data for profits and populations from the cities.
You would like to use this data to help you select which city to expand to
next. The file ex1.txt contains data for the problem. The first column is
population of a city and second column is profit. Both values are in 10,000s.
A negative value of profit indicates a loss.
a) Create a scatterplot between population and profits
b) Develop an ML model to predict profit for a given city (by providing
population)
"""

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


#import and prep tain data
data= pd.read_csv('/home/ai21/Desktop/common/ML/Day5/ML_Assignments/ex1.txt', delimiter=',')
data=data.as_matrix()
X1= data[:,0]
y1= data[:, 1]
X=X1.reshape(-1,1)
y=y1.reshape(-1,1)

#scatter plot

plt.scatter(X,y)
plt.xlabel("population")
plt.ylabel('profits')
plt.show()

#ML model train and predict
lr= LinearRegression()
lr.fit(X, y)
p=lr.predict(17)
print p
