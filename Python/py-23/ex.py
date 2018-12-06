"""
0.import pandas 
1.Create a (4,4)2D array  consisting of integers.
2.Create a masked array from the above array by making numbers which are divisible by 3 as invalid values.
3.Create a dataframe from the above masked array.
4.Create a series of your own choice and do reindexing by exploring ffill,bfill,nearest etc
5.Create a Dataframe object of your own choice and do reindexing.
"""

import pandas as pd
import numpy as np
from pandas import DataFrame as df

#123
a1=np.arange(0,16).reshape(4,4)
a2=np.ma.masked_array(a1, mask=a1%3==0)
print a1,a2
df1=df(a2)

print df1

s1= df1[0]
print s1, type(s1)
print "\n===============\n\n"
s2=s1.fillna(0)
print s2

#5
print "\n===============\n\n"
dataf= df(np.arange(1,10).reshape(3,3))
dataf=dataf.reindex(list((2,1,0,4)), method='ffill')
print dataf


"""
6.Create a (4,4)2D array  consisting of integers.
7.create a dataframe object from the above array by making c1,c2,c3,c4 as column indices and r1,r2,r3,r4 as row indices.
        2.1 Using integer based indexing print the very first element(row 0, column 0) as a scalar,as a series,and as a dataframe.
        2.2 do 2.1 using label based indexing
        2.3 Print last two rows and columns

8.Create another (4,4)2D array  consisting of integers, with c1,c2,c5,c6 as column indices and r3,r4,r5,r6 as row indices
        Create a dataframe from this array and do the following,
        a) add the two dataframes(QNo.7) using '+' operator,withoou any NaN in the result
        b) add the two dataframes using 'add' method,withoou any NaN in the result
9.Create DataFrame obj(shape 3,4) and from that create two Series objs(one for axis 0,other for axis 1)
        perform subtraction operation for both cases(along the two axes)
"""

#6,7
print "\n===============\n\n"
df6= df(np.arange(1,17).reshape(4,4), columns=('c1 c2 c3 c4').split(), index=('r1 r2 r3 r4').split())
print df6, "\n", df6.iloc[0,0], "\n", df6.iloc[0][[0]], "\n",df6.iloc[[0],[0]],'\n\n'

print "\n", df6.loc['r1','c1'], "\n", df6.loc['r1'][['c1']], "\n",df6.loc[['r1'],['c1']],'\n\n'
print df6.iloc[2:,2:]

#8

print "\n===============\n\n"
df7= df(np.ones((4,4)), columns=('c1 c2 c5 c6').split(), index=('r3 r4 r5 r6').split())
print (df6+df7).fillna(0)
print df6.add(df7, fill_value=0).fillna(-1)

#9
print "\n===============\n\n"
df9= df(np.arange(1,13).reshape(3,4))
print df9,'\n\n'
s09 = df9.iloc[0]
s19 = df9.iloc[:,0]
print s09, '\n\n',s19, '\n\n'
print df9.sub(s09, axis=1)
print df9.sub(s19, axis=0)



