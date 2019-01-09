"""
Implement Model Check Points in a model developed for Fashion MNIST
Dataset in keras.
"""

#fashion mnist dataset prediction using Keras
from keras.datasets import fashion_mnist
from keras import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from keras.utils.np_utils import to_categorical
from keras.callbacks import ModelCheckpoint
import os.path

#load data
(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()
print X_train.shape, X_test.shape, y_train.shape, y_test.shape
weights_resume='/home/ai21/Ex-Rufza/ML/ML-20/weights1.hdf5'

#transform data
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

    #change y to one hot encoded format
n_classes=10
y_train=to_categorical(y_train, n_classes)
y_test=to_categorical(y_test, n_classes)



#hyperparameters
filter_num=32
n_conv=3
n_pool=2
batch_size=200
n_epochs=1

#create model
model=Sequential()
model.add(Conv2D(filter_num,kernel_size=(n_conv,n_conv), input_shape=(height,width,1), activation='relu'))
model.add(Conv2D(filter_num,kernel_size=(n_conv,n_conv), activation='relu'))
model.add(MaxPooling2D(pool_size=(n_pool, n_pool)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(n_classes, activation='softmax'))

#load existing weights
if os.path.isfile(weights_resume):
    print "WEIGHTS RESUMED FROM FILE \n"
    model.load_weights(weights_resume)
else:
    print "NO WEIGHTS LOADED"
#compile model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

#add modelcheckpoint
filename='weights1.hdf5'
checkpoint=ModelCheckpoint(filename, monitor='val_acc', verbose=1, save_best_only=True, mode='max')
callback_list=[checkpoint]
#train model
model.fit(X_train,y_train, batch_size=batch_size, epochs=n_epochs, validation_data=(X_test, y_test), callbacks=callback_list)

#predict model
loss,accuracy= model.evaluate(X_test, y_test, verbose=0)
print "LOSS ACCURACY: ", loss, accuracy

