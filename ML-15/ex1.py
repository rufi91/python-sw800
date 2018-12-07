"""
Develop a model to do iris classification problem using Keras
Sequential model. Run the model for varying number of epochs
and batch sizes and observe the accuracy
"""

from sklearn.datasets import load_iris
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from sklearn.preprocessing import OneHotEncoder


data=load_iris()
X=data.data
y=data.target.reshape(-1,1)

#encode data
encoder=OneHotEncoder()
y=encoder.fit_transform(y)

#create and train model with different epoch and batch size

batch_sizes=[100,150,200,]
epochs=[50,150,200]

for e in epochs:
    for b in batch_sizes:
        model=Sequential()
        model.add(Dense(4, input_shape=(4,), activation='relu'))
        model.add(Dense(10, activation='relu'))
        model.add(Dense(3, activation='softmax'))
        optimizer=Adam(lr=0.001)
        model.compile(optimizer, loss='categorical_crossentropy',metrics=['accuracy'])
        model.fit(X,y, verbose=0,epochs=e, batch_size=b)
        #check accuracy
        results= model.evaluate(X,y)
        print "For model batch size %d, epoch %d"%(b,e),results[0], results[1]
        print "\n====================================\n"

"""
OUTPUT

2. Develop a model to do classification in the sonar.csv dataset.

150/150 [==============================] - 0s 2ms/step
For model batch size 100, epoch 50 1.08496054729 0.333333333333

====================================

150/150 [==============================] - 0s 1ms/step
For model batch size 150, epoch 50 1.53349893888 0.333333333333

====================================

150/150 [==============================] - 0s 2ms/step
For model batch size 200, epoch 50 0.925298528671 0.420000000199

====================================

150/150 [==============================] - 0s 1ms/step
For model batch size 100, epoch 150 0.361914871534 0.973333333333

====================================

150/150 [==============================] - 0s 2ms/step
For model batch size 150, epoch 150 0.960352995396 0.66

====================================

150/150 [==============================] - 0s 2ms/step
For model batch size 200, epoch 150 1.21040058613 0.0133333333333

====================================

150/150 [==============================] - 0s 2ms/step
For model batch size 100, epoch 200 1.09861334642 0.333333333333

====================================

150/150 [==============================] - 0s 2ms/step
For model batch size 150, epoch 200 1.09856136163 0.34

====================================

150/150 [==============================] - 0s 2ms/step
For model batch size 200, epoch 200 1.07972308477 0.333333333333

====================================

"""
