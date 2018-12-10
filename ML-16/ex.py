"""
1) Implement a Convolutional Neural Network Model for MNITST(Modified National
Institute of Standards and Technology database) dataset for handwritten digits.
Obtain the maximum accurate model. Print the loss and accuracy values.
2) using fashion_mnitst
"""
import numpy as np
from keras.datasets import mnist, fashion_mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.utils.np_utils import to_categorical #to convert categorical to numerical
import matplotlib.pyplot as plt


#load data
(X_train, y_train),(X_test, y_test)=fashion_mnist.load_data()

#print X_train1.shape, y_train1.shape, X_test1.shape, y_test1.shape
"""

(X_train, y_train),(X_test, y_test)= mnist.load_data()
print "SHAPE:",X_train.shape"""
    #dim of data
n_train, height, width = X_train.shape
n_test, _, _ = X_test.shape
print n_train, n_test, height, width

#transform data
X_train = X_train.reshape(n_train, height, width, 1).astype('float32')
X_test = X_test.reshape(n_test, height, width, 1).astype('float32')
print "SHAPE:", X_train.shape #QUESTION:WHY DO WE RESHAPE TO (X,Y,Z,1)?

    #normalize data
X_train/=255
X_test/=255
n_classes=10

y_train=to_categorical(y_train, n_classes)
y_test=to_categorical(y_test, n_classes)

#create filters
n_filters=32
n_conv =3 #filter size
n_pool= 2 #pooling window size

#create model
model= Sequential()
model.add(Convolution2D(n_filters, kernel_size=(n_conv,n_conv), input_shape=(height,width,1), activation='relu'))
model.add(Convolution2D(n_filters, kernel_size=(n_conv, n_conv),activation='relu'))
model.add(MaxPooling2D(pool_size=(n_pool,n_pool)))
model.add(Dropout(0.25))
    #flatten the data for the 1D layers
model.add(Flatten())
model.add(Dense(128,activation='relu')) 
model.add(Dropout(0.5))
model.add(Dense(n_classes, activation='softmax')) #softmax gives us probability of each class

#compile model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

#train model
batch_size=128
n_epochs=1
model.fit(X_train,y_train,batch_size=batch_size, epochs=n_epochs, validation_data=(X_test, y_test)) #why do we pass in validation data?

#test model
loss,accuracy = model.evaluate(X_test,y_test, verbose=0)
print "\\nLOSS: ", loss
print "\nACCURACY ", accuracy
x_sample = X_test[0].reshape(1,28,28,1)
y_prob = model.predict(x_sample)[0]
y_pred = y_prob.argmax()
y_actual = y_test[0].argmax()

image_index = 0
plt.imshow(X_test[image_index].reshape(28, 28),cmap='Greys')
plt.show()

print("probabilities: ", y_prob)
print("predicted = %d, actual = %d" % (y_pred, y_actual))

