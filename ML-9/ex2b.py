"""
Apply Standardization/ Normalization to the required columns in
banking.csv dataset and check whether any improvement in accuracy is
obtained.
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score,train_test_split,KFold
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import *
from sklearn import preprocessing
from matplotlib import pyplot as plt
import pandas as pd

#d. banking dataset (bank.csv) linear regression best
data=pd.read_csv('/home/ai21/Ex-Rufza/ML/ML-7/bank.csv', delimiter=',')
data=data.as_matrix()
X=data[:,(0,11,12,13,15,16,17,18,19)]
X1=preprocessing.scale(data[:,(0,11,12,13,15,16,17,18,19)])
X2=preprocessing.normalize(data[:,(0,11,12,13,15,16,17,18,19)])
y=data[:,-1]
y=y.astype(int)
X_train,X_test,y_train, y_test= train_test_split(X, y , test_size=0.2)
X1_train,X1_test,y_train, y_test= train_test_split(X1, y , test_size=0.2)
X2_train,X2_test,y_train, y_test= train_test_split(X2, y , test_size=0.2)

print X.shape, y.shape

#prepare model

rft=LogisticRegression()
rft.fit(X_train, y_train)
p=rft.predict(X_test)

rft.fit(X1_train, y_train)
p1=rft.predict(X1_test)

rft.fit(X2_train, y_train)
p2=rft.predict(X2_test)


#print accuracy:
print "\n Accuracy without standardization: ", accuracy_score(y_test,p)
print "\n Accuracy with standardization: ", accuracy_score(y_test,p1)
print "\n Accuracy with normalization: ", accuracy_score(y_test,p2)

