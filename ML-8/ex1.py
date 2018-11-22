"""
Develop an ML model to predict the house price for the boston
housing dataset included in sklearn. Find out the RMSE values for
models developed using different algorithms and select the best one.
Also plot the scatter diagrams showing the actual and predicted values
"""

from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from matplotlib import pyplot as plt
from sklearn.metrics import mean_squared_error
from numpy import *

#KNN, SVM, Decision Tree, Random Forest
#prepare data
data=load_boston()
X=data.data
y=data.target
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)

#prepare and train models

knn=KNeighborsRegressor()
knn.fit(X_train, y_train)

svr=SVR()
svr.fit(X_train, y_train)

dtree= DecisionTreeRegressor()
dtree.fit(X_train, y_train)

rforest= RandomForestRegressor()
rforest.fit(X_train, y_train)

#predict all models
p1=knn.predict(X_test)
p2=svr.predict(X_test)
p3=dtree.predict(X_test)
p4=rforest.predict(X_test)

#print rmse of all
print "\n\n =============RMSE REPORT===============\n\n"

print "KNR:  ", sqrt(mean_squared_error(p1,y_test)), "\n"
print "SVR:  ", sqrt(mean_squared_error(p2,y_test)), "\n"
print "DTree:  ", sqrt(mean_squared_error(p3,y_test)), "\n"
print "RForest:  ", sqrt(mean_squared_error(p4,y_test)), "\n"


#plot

plt.scatter(y_test,p1)
plt.xlabel("actual values")
plt.ylabel("predicted values")
plt.title("KNR")
plt.show()

plt.scatter(y_test,p2)
plt.xlabel("actual values")
plt.ylabel("predicted values")
plt.title("SVR")
plt.show()

plt.scatter(y_test,p3)
plt.xlabel("actual values")
plt.ylabel("predicted values")
plt.title("DTree")
plt.show()

plt.scatter(y_test,p4)
plt.xlabel("actual values")
plt.ylabel("predicted values")
plt.title("Rforest")
plt.show()

p=rforest.predict(X_test)

#rmse
