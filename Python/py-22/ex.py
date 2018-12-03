"""
A.Open python interpreter/ipython and do the following.
	1.import pandas library
	2.create a dataframe obj from a dict of lists of your own choice(other than population) 
	3.Add another column on the above object and insert values.  
	
	
	
	.
	.
	
	
 """
import pandas as pd
import numpy as np
from pandas import DataFrame as df
from pandas import Series as s

dic1={ 'student':['S1','S2','S3'],\
'studid':[199,198,120],\
'marks':[78,88,80] }

dataframe1=df(dic1, columns=['student','studid','marks'])
print dataframe1

dataframe1=df(dic1, columns=['student','studid','marks','dept'])
print dataframe1
#dataframe1.fillna(0)
dataframe1['dept']=['sci','mat','bio']
print dataframe1

#4.create a dataframe obj from a series obj of your own choice.
l1=np.arange(6,20)
ser1=s(l1)
df2=df(ser1, columns=['ADF'])
print df2

#5.create a dataframe obj from the above series obj(Qno.4) after assigning a value for name attribute.
ser1.name ='NAMESERIES'
df3=df(ser1)
print df3

#6.create a dataframe object from a numpy 2D array by giving values for columns and index of your own choice.

l1=np.arange(1,10).reshape(3,3)
df6=df(l1, index=list('abc'), columns=['x','y','z'])
print df6

#7.create a nested dictionary to store employee details like empno,empname and salary.create a dataframe from this dict
dic2={ 'empname':['Ram','Shyam','S3'],\
'empno':[199,198,120],\
'salary':[78,88,80] }

df7=df(dic2)

#8.create a series object to contain designations of the above employees, assign 'desig' as the name to this series object
desig = s(['sci','proff','asst'])
print desig


#9.Add the above series object to the dataframe object and the column name should be the same as series name.

df7['desig']=df(desig)
print df7

#10.Create two series objects with values (1,2 ... 6) and (11,22 ... 66),indices (a,b,c,d,e,f) and (d,e,f,x,y,z) respectively.
#Add the two series objects, the result should contain 9 nonzero values. (use reindex)

ss1=s(np.arange(1,7), index=list('abcdef'))
ss2=s(np.arange(11,77, 11), index=list('defxyz'))
i1=ss1.index
i2=ss2.index
#both ss1 and ss2
i3=i1.intersection(i2)
print i3
ss3= ss1[i3] +ss2[i3] #DEF
print "===intersection=== \n",ss3

#in only ss1 in only ss2
i4=i1.difference(i2)

s1=ss1[i4] #ABC
s=s1.append(ss3)
print "======= \n only ss1",s


i4=i2.difference(i1) #xyz
s2=ss2[i4]
print "======= \n only ss1",s2
p=s.append(s2)
print "============ \n final",p

