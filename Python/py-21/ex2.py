"""
B.Open python interpreter/ipython and do the following.
	1.import pandas library
	2.print the verion of pandas
	3.create a series object having 5 elements
	4.print all the elements
	5.print first two elements
	6.create another series object by supplying string labels as index
	7.print all the elements/print individual elements
	8.create a dict object and then  a series object from that dictionary  
	9.create another dict obj with some common keys (Q.No.8) and then a series obj
	10.add the two Series objs and print the result.
	"""
import pandas as pd
from pandas import Series as s
import numpy as np

print pd.__version__,"\n"

l1=np.arange(1,6)
s1=s(l1)
print s1
print s1[[0,1]]

l2=np.arange(6,11)
s2=s(l2, index=list('abcde'))
print s2.values

d1={ 'a':10, 'b':20, 'c':30, 'd':40}
s3=s(d1)
print s3.values


d2={ 'a':11, 'z':22, 'y':33, 'k':44}
s4=s(d2)
print s4.values

s5=s3.append(s4)
print "===========\n ",s5


