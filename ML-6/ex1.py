"""
Develop an ML model for predicting the digits in the digits image dataset in
sklearn using SVM . Plot some sample input images together with its class
information. Also plot some predicted outputs together with its actual
images.
[hint: To plot the images using plt.imshow use the actual dimension of the
images in the dataset. Before fitting the data to the SVC model reshape the
X data from (n,8,8) to (n, 64) using X.reshape(n,-1) where n is the number of
images]
"""

from sklearn.svm import SVC
from sklearn.datasets import load_digits
from sklearn.metrics import classification_report,confusion_matrix
import  matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

data=load_digits()
X=data.images
y=data.target

print "==================\n before reshape",X.shape
"""
#plotting existing data
#The zip() function returns an iterator of tuples based on the iterable object.
ilabels=list(zip(X,y))
for index,(image,label) in enumerate(ilabels[:4]):
	plt.subplot(2,4,index+1)
	plt.axis('off')
	plt.imshow(image,cmap=plt.cm.gray_r,interpolation='nearest')
	plt.title(label)
plt.show()

print(X.shape)
#X is an ndarray (m,n,n)

"""
n=len(X)
X=X.reshape(n,-1)
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.5)

#creating the model, training and fitting
model=SVC(gamma=0.001)
model.fit(X_train,y_train)
p=model.predict(X_test)

#printing metrics
print(confusion_matrix(y_test,p))
print(classification_report(y_test,p))

n1=len(X_test)
X_test=X_test.reshape(-1,8,8)

#plotting predicted values
ilabels=list(zip(X_test,p))
for index,(image,label) in enumerate(ilabels[:4]):
        plt.subplot(2,4,index+1)
        plt.axis('off')
        plt.imshow(image,cmap=plt.cm.gray_r,interpolation='nearest')
        plt.title(label)
plt.show()

