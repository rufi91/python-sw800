"""

One of the reasons that the shipwreck led to such a loss of life was that there
were not enough lifeboats for the passengers and crew. Although there was
some element of luck involved in surviving the sinking, some groups of
people were more likely to survive than others, such as women, children, and
the upper-class.
Develop an ML model to predict the survival of passengers.
"""

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
import numpy as np


#import and prep tain data
data= pd.read_csv('/home/ai21/Desktop/common/ML/Day5/ML_Assignments/titanic.csv', delimiter=',')

print "=======Null: \n\n",data['Age'].isnull().sum()
agemean=data['Age'].mean()
print "=======Mean: \n\n",agemean
data['Age'].fillna(agemean, inplace=True)
print "=======Null: \n\n",data['Age'].isnull().sum()

data=data.as_matrix()
sex= data[:,4]
  #change from string to num
enc= preprocessing.LabelEncoder()
enc.fit(sex)
data[:,4]= enc.transform(sex)

X= data[:,[2,4,5]]
y= data[:, 1].astype('int')
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)

#ML model train and predict
lr= LogisticRegression()
lr.fit(X_train, y_train)
p=lr.predict(X_test)
print p
print '\n =============Accuracy=============\n\n',accuracy_score(y_test,p)



