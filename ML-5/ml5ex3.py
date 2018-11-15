"""
Suppose you are selling your house and you want to see what a good market
price would be. The ex2.txt contains a training set of housing prices in India.
The first column is the size of the house (in square feet). The second column
is the number of bedrooms and the third column is the price of the house.
a) Use scatter plots to visualize the data
b) Develop an ML model to predict the house price.
"""


import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


#import and prep tain data
data= pd.read_csv('/home/ai21/Desktop/common/ML/Day5/ML_Assignments/ex3.txt', delimiter=',')
data=data.as_matrix()
X= data[:,(0,1)]
y= data[:, 2]
print X.shape
print y.shape
print y
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)

#scatter plot

plt.scatter(X[:,0],X[:,1], c=y)
plt.xlabel("score1")
plt.ylabel('score2')
plt.show()


#ML model train and predict
lr= LogisticRegression()
lr.fit(X_train, y_train)
p=lr.predict(X_test)
print p


