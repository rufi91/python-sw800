"""1. Write a python script to create and store a 2D array as a file by receiving 
		start and end numbers from user.
		The array should contain elements from 
		start to end incremented by 1.
		A suitable shape can be 
		decided by the programmer.
		0 can be used to fill columns if required.
		From this array, using conditional logic, create two new arrays , consisting of
		elements which are divisible by a given number,say dn1, in the first array
		 and not divisible by dn1 in the second array.
"""
import numpy as np

start= input("Enter start range: ")
end= input("Enter end range: ")


arr=np.arange(start,end+1).reshape(3,-1)
print arr
np.save('arrfile',arr)

arr1=np.load('arrfile.npy')
print "The saved array from file is : \n",arr1

a1=np.where(arr%5==0,arr,-1)

a2=np.where(arr%5!=0,arr,-1)

a=a1[a1!=-1]
print "\n Numbers divisible: ", a

a=a2[a2!=-1]
print "\n Numbers not divisible: ", a
