"""
Open python interpreter/ipython and do the following.

	0.import pandas 
	1.create a dataframe object from a (10,4)2D array  consisting of random integers between 10 and 20 by making c1,c2,c3,c4 as column indices.
	2.Sort the above oject based on the key 'c1' in ascending and then by 'c3' in descending order.
	
"""

import numpy as np
import pandas as pd
from pandas import Series as s
from pandas import DataFrame as df

l1=(np.random.randint(10,20, 40)).reshape(10,4)
print l1

df1=df(l1, columns=['c1','c2','c3','c4'])
print df1

df1.sort_values(['c1','c3'], ascending=[True,False])

"""
3.write script to store item,place and total sale in a dataframe object.There should be 3 or more places and 4 or more items in the set.
	     Based on the choice entered by user, 	
           (ii) show placewise rank for a particular item (for a given item name).
	   (iii)Show itemwise rank for a particular place (for a given place name).
"""	   """

dic1= {'item':['apple','banana','orange','grape','apple','orange'],\
       'place':['kochi','tvm','clt','kochi','clt','tvm'],\
       'sales':[200,100,220,300,450,190]}

df2=df(dic1)
item1= raw_input("Enter the item required: ")

#df2=df2.sort_values(['item','sales'], ascending=[True,False])
df2=df2[df2['item']==item1]
print df2

df2['rank']=df2['sales'].rank(ascending=False)
print df2
##################################

place1= raw_input("Enter the place required: ")
df3=df(dic1)

df3=df3[df3['place']==place1]
print df3

df3['rank']=df3['sales'].rank(ascending=False)
print df3


4.switch to home directory and send the output of ls -l command to a file named lsf1  
	5.create another file lsf2 by replacing all the spaces with ',' use tr command tr ' ' ',' < lsf1 > lsf2
	6.create another file lsf3 by squeezing multiple ',' use tr command - tr -s ',' < lsf2 > lsf3
	7.using pandas read the file lsf3 and sort it based on file size (fifth column)
	8.write the above dataframe obj (sorted) to a new file named lsf5
	"""

df4=pd.read_csv('/home/ai21/lsf3.txt', delimiter=',')
print df4,"\n",df4.shape,"\n"
df4.columns='a b c d f g h i j'.split()
df4=df4.sort_values(['f'])
print df4
df4.to_csv('lsf5.txt')
