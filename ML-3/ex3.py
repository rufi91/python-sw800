"""
Develop an ML model to predict diabetes(last column in the datset) from
the pima Indians dataset using Logistic Regression. This dataset is from the
National Institute of Diabetes and Digestive and Kidney Diseases. The
objective is to predict based on diagnostic measurements whether a
patient has diabetes. Several constraints were placed on the selection of
these instances from a larger database. In particular, all patients here are
females at least 21 years old of Pima Indian heritage (pimaindians.csv )
"""

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

data=pd.read_csv('/home/ai21/Desktop/common/ML/Day3/pimaindians.csv')
data=data.as_matrix()
X = data[:,0:7]
y = data[:,8]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print X_train.shape
print y_train.shape

lr=LogisticRegression()
lr.fit(X_train, y_train)
p=lr.predict(X_test)

print "----------Prediction-----------\n\n",p

print "\n\n-----------Classification Report----------\n\n",classification_report(y_test, p)
