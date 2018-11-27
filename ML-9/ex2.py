"""
Standardization and Normalization
1) Apply Standardization/ Normalization for the immunotherapy problem
(day2) and check whether the accuracy is improved.

"""

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn import preprocessing

train1=pd.read_csv("/home/ai21/Desktop/common/ML/Day2/Questions/Immunotherapy.csv")
train=train1.as_matrix();
X=train[:,0:7]
X1=preprocessing.scale(train[:,0:7])
X2=preprocessing.normalize(train[:,0:7])
y=train[:,7]
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)
X1_train, X1_test, y_train, y_test = train_test_split(X1,y, test_size=0.2)
X2_train, X2_test, y_train, y_test = train_test_split(X2,y, test_size=0.2)


knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train,y_train)
p=knn.predict(X_test)

print "\n ==========Without scaling:=========== \n"
#print("Prediction: ",p)
print"\n Accuracy Score: ",accuracy_score(y_test,p)
#print("\n Confusion Matrix: ",confusion_matrix(y_test,p))

knn1 = KNeighborsClassifier(n_neighbors=3)
knn1.fit(X1_train,y_train)
p1=knn1.predict(X1_test)
p4=knn.predict(X1_test)

print "\n ==========With scaling:=========== \n"
#print("Prediction: ",p1)
print"\n Accuracy Score: ",accuracy_score(y_test,p1)
print"\n Accuracy Score####: ",accuracy_score(y_test,p4)
#print("\n Confusion Matrix: ",confusion_matrix(y_test,p1))

knn2 = KNeighborsClassifier(n_neighbors=3)
knn2.fit(X2_train,y_train)
p2=knn2.predict(X2_test)


print "\n ==========With normalization:=========== \n"
#print("Prediction: ",p2)
print"\n Accuracy Score: ",accuracy_score(y_test,p2)
#print("\n Confusion Matrix: ",confusion_matrix(y_test,p2))
