"""
Train a machine learning model that is able to predict the facies for wells not in
the training set.
Data set (mining.csv)
The data set we will use comes from University of Kansas. This dataset was taken
from nine wells with 3232 examples, consisting of a set of seven predictor
variables and a rock facies (class).

"""


import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

#import and prep tain data
data= pd.read_csv('/home/ai21/Desktop/common/ML/Day5/ML_Assignments/mining.csv', delimiter=',')

data=data.as_matrix()
X= data[:,3:10]
y= data[:, 0].astype('int')
print X.shape
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)

knn = KNeighborsClassifier(n_neighbors=15)
knn.fit(X_train,y_train)
p=knn.predict(X_test)

print '\n =============Prediction=============\n\n',p
print '\n =============Accuracy=============\n\n',accuracy_score(y_test,p)


