##### PLOTTING LESS GREATER THAN 50 #########
import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure(figsize=(6,6), facecolor='0.8')
sb1=fig.add_subplot(1,1,1)
y= np.random.randint(1,100,10)
y1=y[y<50]
y2= y[y>=50]
x= np.arange(2,21,2)
print (y,'\n',y1,'\n',y2,'\n',x)
y2=np.insert(y2,0,y1[-1])
print (y2)
sb1.plot(x[0:y1.size],y1,'ro:')
sb1.plot(x[y1.size-1:],y2,'bo--')
sb1.set_title("MATPLOTLIB")
sb1.set_xlabel("X AXIS")
sb1.set_ylabel("Y AXIS")
plt.show()


############ GROUP OBJECT ###################
import pandas as pd

drinks=pd.read_csv('/home/ai21/Desktop/common/Python_Exercises/drinks.csv')
drinkobj=drinks.groupby('continent')


print "\nPrint the continent that drinks more beer on average: ", drinkobj.sum()['beer_servings'].max()
print drinkobj.sum()['beer_servings'].nlargest(1)
print drinkobj.sum()['beer_servings'].idxmax()

print "\n\nFor each continent print the statistics(count,mean,std etc.) for wine consumption.:\n",drinkobj.describe()['wine_servings']

print "\n\nPrint the mean alcoohol consumption per continent for every column:\n",drinkobj.mean()

print "\nmedian alcoohol consumption per continent for every column\n", drinkobj.agg('median')

print "\n\n Print the mean, min and max values for spirit consumption.: \n", drinkobj.agg(['mean','min','max'])['spirit_servings']


##############MYSQL ##################
import pandas as pd
import MySQLdb as my
from sqlalchemy import create_engine as ce
from pandas import DataFrame as df

ef1=pd.read_csv('/home/ai21/Desktop/common/Python_Exercises/emp.csv', header=None, names='name empno desig salary deptcode'.split())

ef1['deptcode']=[121,122,123,121,121,123,122,121,121,124]
print ef1

ce1=ce("mysql://ai:ai@127.0.0.1/ai")
#ef1.to_sql("ai_21_emp", ce1)

dic1={ 'dept_no':[121,122,123,124],\
'dept_name':['CSE','ECE','MECH','IT'],\
'dept_location':['B2F0','B3F2','B1F1','B3F1'] }

df1=df(dic1, columns=['dept_no','dept_name','dept_location'])
#df1.to_sql("ai_21_dep", ce1)

con=my.connect('127.0.0.1','ai','ai','ai')
ef2=pd.read_sql("select * from ai_21_emp",con)
df2=pd.read_sql("select * from ai_21_dep",con)

df3=ef2.merge(df2,left_on='deptcode', right_on='dept_no')[['empno','name','dept_name','salary']].sort_values(['salary'])
print df3
#df3.to_sql("ai_21_emp_dep", ce1)

##################### DF MANIPULATION REGEX ###########
import pandas as pd
from pandas import DataFrame as df
import re


ef1=pd.read_csv('/home/ai21/Desktop/common/Python_Exercises/emp.csv', header=None, names='name id desig sal phno'.split())
print ef1
ef2=ef1.copy()
ef2['phno']= ef1['phno'].apply(lambda n: re.sub('[^0-9\.]','',str(n)))
print ef2

#3.Write the three columns ename,edesig and esalary to the excel file empx.xlsx with sheet name as salary

writeObj= pd.ExcelWriter('empx.xlsx')
ef2.to_excel(writeObj, 'salary', columns=list(('name', 'id','sal')))

#4.Write the two columns ename and  ephno to the same excel file empx.xlsx with sheet name as phone 

ef2.to_excel(writeObj, 'phone', columns=list(('name', 'phno')))

#5.In the data frame ef2 make edesig and eno as row index & store the new data in ef3
ef3=ef2.set_index(['desig','id'])
print ef3

#6.In ef3, sort the index edesig and store the result in ef4
ef4=ef3.sort_index(level='desig')
print ef4

#6.1.Using ef4, display all the scientists records
print ef4.loc['scientist']

#6.2.Display average salary of engineers.
print ef4.loc['engineer'].mean()['sal']


########## DICT DF ###########
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
place1= raw_input("Enter the place required: ")
df3=df(dic1)
df3=df3[df3['place']==place1]
print df3
df3['rank']=df3['sales'].rank(ascending=False)
print df3


########### ADD 2 DF #################

import pandas as pd
import numpy as np
from pandas import DataFrame as df
df6= df(np.arange(1,17).reshape(4,4), columns=('c1 c2 c3 c4').split(), index=('r1 r2 r3 r4').split())
df7= df(np.ones((4,4)), columns=('c1 c2 c5 c6').split(), index=('r3 r4 r5 r6').split())
print ((df6+df7).fillna(0))
print( df6.add(df7, fill_value=0).fillna(-1))



######### SERIES FROM DF ############
df9= df(np.arange(1,13).reshape(3,4))
print df9,'\n\n'
s09 = df9.iloc[0]
s19 = df9.iloc[:,0]
print s09, '\n\n',s19, '\n\n'
print df9.sub(s09, axis=1)
print df9.sub(s19, axis=0)


############ ALOT OF SERIES AND DF - DAY22#############
############ DF SCIENTIST MANIPULATION DAY 20 ##############
import numpy as np

datatype= np.dtype([('ename','S20'),('eno','i8'),('edesig','S20'),('esal','f8'),('ephn','S20')])
filedata = np.loadtxt('/home/ai21/Desktop/common/Python_Exercises/emp.csv', delimiter=',', dtype= datatype)
print filedata

print "\n ============Names:================= \n", filedata['ename']
print "\n ============Names of officers:================= \n", filedata[filedata['edesig']=='officer']['ename'] 
print "\n ============Scientist Records:================= \n", filedata[filedata['edesig']=='scientist'] 
print "\n ============Total salary:================= \n", filedata['esal'].sum()
print "\n ============Avg salary of engineers:================= \n", filedata[filedata['edesig']=='engineer']['esal'].mean()
filedata.sort(order='esal')
print "\n ============Asc order of salary:================= \n", filedata
filedata.sort(order='esal')
filedata.sort(order='edesig')
print "\n ============Asc order of Desig-salary:================= \n", filedata
fd1=filedata.copy()
fd1.sort(order='esal')
print "\n ============Lowest Sci salary:================= \n", fd1['esal'][0]

lsal=filedata[filedata['edesig']=='scientist']['esal'].min()
sci=filedata[filedata['edesig']=='scientist']

print "\n ============Lowest Sci salary without sort:================= \n", sci[sci['esal']==lsal]


############## TOTAL SALES CALCULATION MATRIX DOT DAY 19 EX3############
############
