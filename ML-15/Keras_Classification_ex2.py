"""
2. Develop a model to do classification in the sonar.csv dataset.
"""

from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
import pandas as pd

data=pd.read_csv('sonar.csv').as_matrix()
X=data[:,0:60]
y=data[:,-1]
print X.shape, y.shape

#encode data
lencoder=LabelEncoder()
lencoder.fit(y)
y=lencoder.transform(y).reshape(-1,1)
encoder=OneHotEncoder()
y=encoder.fit_transform(y)

#Create and train model
model=Sequential()
model.add(Dense(60, input_shape=(60,), activation='relu'))
model.add(Dense(20, activation='relu'))
model.add(Dense(2, activation='softmax'))
optimizer=Adam(lr=0.001)
model.compile(optimizer, loss='categorical_crossentropy',metrics=['accuracy'])
model.fit(X,y, verbose=0,epochs=200, batch_size=50)
#check accuracy
results= model.evaluate(X,y)
print results[0], results[1]
print "\n====================================\n"


