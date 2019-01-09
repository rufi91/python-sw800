import tensorflow as tf
import numpy as np

#params
learning_rate=0.001
epochs=5000
display_epoch=50
X_train = np.asarray([3.3,4.4,5.5,6.71,6.93,4.168,9.779,6.182,7.59,2.167,7.042,10.791,5.313,7.997,5.654,9.27,3.1])
Y_train = np.asarray([1.7,2.76,2.09,3.19,1.694,1.573,3.366,2.596,2.53,1.221,2.827,3.465,1.65,2.904,2.42,2.94,1.3])
n_samples=X_train.shape[0]

#create model y=mx+c
X=tf.placeholder('float')
Y=tf.placeholder('float')
m=tf.Variable(np.random.randn(), name='weight')
c=tf.Variable(np.random.randn(), name='bias')
pred=tf.add(tf.multiply(m,X),c)

#create cost= mean error function sum((pred-y)^2)/n
cost= tf.reduce_sum(tf.pow(pred-Y,2)/n_samples)

#create optimizer to minimize cost
optimizer= tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

#create session and run in loop
#initialize variables
init=tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    #fit all training data:
    for epoch in range(epochs):
        for (x,y) in zip(X_train,Y_train):
            sess.run(optimizer, feed_dict={X:x,Y:y})
            if (epoch+1)%50==0:
                cost1=sess.run(cost, feed_dict={X:X_train, Y:Y_train})
                print "Epoch # ", epoch, " Cost: ", cost1, "m: ", sess.run(m), "c: ", sess.run(c),"\n"

    print "OPTIMIZATION COMPLETE!\n"
    print "Final cost, m, c values:", sess.run(cost, feed_dict={X:X_train, Y:Y_train}), sess.run(m), sess.run(c)
