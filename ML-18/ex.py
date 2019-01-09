import tensorflow as tf

#1Create a tensor of the shape [2, 3] with all elements set to zero.
x= tf.zeros([2,3])


#2
X= tf.constant([[1,2,3],[4,5,6]])
x1= tf.zeros_like(X)

#3
x2= tf.ones([2,3])

#4
x3=tf.ones_like(X)

#5
x4= tf.constant([[5,5],[5,5],[5,5]])

#6
x5= tf.constant([[1,3,5],[4,6,8]], tf.float32)

#7
x6= tf.constant([[4,4,4],[4,4,4]])

#8
x7=tf.linspace(5.0,10.0,50)


#9
x8=tf.random_normal([3,2], mean=0, stddev=2)

#10
x9=tf.random_uniform([3,2], minval=0, maxval=2)

#11
XX=tf.constant([[1,2],[3,4],[5,6]])
x10=tf.random_shuffle(XX)

#12
Y=tf.random_normal([10,10,3])
x11=tf.random_crop(Y,[5,5,3])

#13
A=tf.constant([[-1,-2,-3],[0,1,2]])
b= tf.zeros_like(A)
x12= tf.not_equal(A,b)


#14
B=tf.constant([[5,4,2],[1,0,7]])
x14=tf.add(A,B)


#15
x15=tf.subtract(B,A)


#16
x16=tf.multiply(A,B)


#17
x17=tf.multiply(A,5)


#18
C=tf.constant([[1,1,1],[1,0,0]])
x18=tf.add(tf.add(A,B),C)



#19
#writer=tf.summary.FileWriter('./tb',sess.graph)
#writer.close()
#sess.close()

#20
w=tf.constant(1.0)
sess= tf.Session()
output=sess.run(w)
print output

