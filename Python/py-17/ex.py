"""
	1. open a python interpreter
	2. import numpy
	3. create a 1D array having 5 elements (integers) using array method
	4. do 3 using arange
	5. create a 3 dimensional array containing 1s(integers), there should be 40 members
	6. print the total number of elements (size) for the above array
	7. Check and explain the difference between array and asarray
	8. Create an identity mtrix of a given specification.
	9. Create an array containing 0s inheriting shape from the array created in Q.No.5
	10.Print the size,shape,dimensions and datatype of all the above arrays.
"""


import numpy as np

a1=np.array([1,2,3,4,5])
print a1, type(a1), a1.dtype

a2=np.arange(1,6)
print a2

a3=np.ones((2,2,10))
print a3, a3.size

#array- a copy is created
a01=np.array(a1)
a01=a01*2

print "\n\nOriginal array:", a1
print "\nNew array using array() times 2:", a01

#asarray - copy not created
print('\n\n=================\n\n')
a02=np.asarray(a2)
print (a02 is a2)
a02=a02*3
print (a02 is a2)
print "\n\nOriginal array:", a2
print "\nNew array using array() times 3:", a02

#I matrix
a4=np.eye(5)
print a4

#9
a5=np.zeros_like(a3)
print a5

#10
print "size", a5.size,"shape",a5.shape, "dim", a5.ndim, "datatype", a5.dtype
