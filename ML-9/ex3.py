"""
gridsearchCV
1) Write a program to get the optimum value of k for a KNN problem using
GridSearchCV
"""

from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
import numpy as np


iris = load_iris();
X=iris.data
y=iris.target

kn=np.arange(3,30)

knn = KNeighborsClassifier()
grid = GridSearchCV(estimator=knn, param_grid=dict(n_neighbors=kn))
grid.fit(X,y)

print grid.best_score_
print grid.best_estimator_.n_neighbors
