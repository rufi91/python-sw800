"""
1) Implement MLPClassifier for iris dataset in sklearn.
a. Print confusion matrix for different activation functions
b. Study the reduction in loss based on the number of iterations.
2) Implement MLPRegressor for boston dataset in sklearn . Print performance
metrics like RMSE, MAE , etc.
"""

from sklearn.neural_network import MLPClassifier, MLPRegressor
import numpy as np
from sklearn.datasets import load_iris, load_boston
from sklearn.metrics import confusion_matrix, mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split

#1
data=load_iris()
X=data.data
y=data.target

X_train,X_test, y_train, y_test = train_test_split(X, y)
activations=list('identity logistic tanh relu'.split())
for a in activations:
    mlp= MLPClassifier(activation=a,verbose=True, hidden_layer_sizes=200, max_iter=500)
    mlp.fit(X_train,y_train)
    p=mlp.predict(X_test)
    print "\n Accuracy matrix for method %s \n"%a,"\n", confusion_matrix(y_test,p)
    
    
    
#2
dataReg=load_boston()
XReg=dataReg.data
yReg=dataReg.target


Xr_train,Xr_test, yr_train, yr_test = train_test_split(XReg, yReg, test_size=0.2)


mlpr=MLPRegressor()

mlpr.fit(Xr_train,yr_train)

pr=mlpr.predict(Xr_test)

print "\n Performance metrics for MLPR: \n\n\t Mean Squared Error: %f \n\t Mean Absolute Error: %f \n\t RMSE: %f"%(mean_squared_error(yr_test,pr),mean_absolute_error(yr_test,pr), np.sqrt(mean_squared_error(yr_test,pr)))


