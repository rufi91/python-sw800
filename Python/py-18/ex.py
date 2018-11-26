

# 1.Create an integer(32bit) array of shape 2,3

import numpy as np

a1=np.ones((2,3),dtype= 'i4')
print a1
print a1.dtype

#2.Create another array using the values from the above array (Qno.1) but with a type of float64
print "======================================== \n"  
a2=np.asarray(a1, dtype='f8')
print a2
print a2.dtype


#3.Create another array using the values from the above array (Qno.1) but with a type of int64
print "======================================== \n"  
a3=np.asarray(a1, dtype='i8')
print a3
print a3.dtype

#4.Create another array using the values from the above array (Qno.1) but with a type of str
print "======================================== \n"  
a4=np.asarray(a1).astype(str)
print a4
print a4.dtype

#5.Create another array using the values from the above array (Qno.4) but with a type of str
print "======================================== \n"  
a5=np.asarray(a4).astype(str)
print a5
print a5.dtype

"""	6. create a 2 dimensional array conating 4 rows and 3 columns each and do different slicing operations and note your findings
		 	-> select first row  
			-> select third row
			-> select second column
		   	-> select first two elements of second and third rows
			-> select last element of each row
				etc."""

a6=np.array([[1,2,3], [4,5,6], [7,8,9],[10,11,12]])
print a6
print a6[0,:],"\n"
print a6[2,:],"\n"
print a6[:,1],"\n", a6[:,1:2],"\n"
print a6[1:3,:2],"\n"
print a6[:,-1]

#7.Create a numpy array(with a suitable shape) to store numbers from 11 to 50.
# using boolean indexing, replace all the numbers that are multiples of 5 with -1.
print "======================================== \n"  
a7=np.ones((10,4))

for i in range(10):
    for j in range(4):
        a7[i][j]=(i*4+j)+11

print a7

a7[a7%5==0]=-1

print a7.size

#8.Write a function to return diagonal elements of an array(NxN) as an array.
print "======================================== \n"  
def diagonal(arr):
    a=[]
    for i in range(int(np.sqrt(arr.size))):
        a.append(arr[i][i])
    print a

a8=np.eye(7)
diagonal(a8)

#9.Write a function to return the number of occurences of a given element in a numpy array.
print "======================================== \n"  
def repeat(arr, element):
    ar1=(arr==str(element))
    print "The total number of element occurrences are: ",arr[ar1].size
         
a9=np.array(['1', '2' , '3', '5', '5', '5', '8'])
repeat(a9,2)

"""
10.Modify the above function (Q.No.8) to accept array of any shape and to return the 
   diagonal elements of the highest possible NxN array constructed from the given array. 
"""
print "======================================== \n" 

def diagonal1(arr):
    print arr.shape
    size=min(arr.shape[0], arr.shape[1])
    print size
    a=[]
    for i in range(size):
        a.append(arr[i][i])
    print a

a10=np.random.randint(low=10, high=100, size=70).reshape(7,10)
print a10
diagonal1(a10)




