"""
Develop a KNN model and do accuracy computation with cross validation. Also
obtain Precision , Recall and F1 Score using classification report.
"""

from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import classification_report


iris = load_iris();
X=iris.data
y=iris.target

knn = KNeighborsClassifier(n_neighbors=3)
score=cross_val_score(knn,X,y, cv=10)
print "==========Cross Val Score=========",score

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)
print("Dimensions of data sets:")
print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)

knn.fit(X_train,y_train)
p=knn.predict(X_test)
print("Prediction: ",p)
print"=======Classification Report========= \n\n ",classification_report(y_test,p)


