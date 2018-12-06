"""
 1. Create a mysql table ai_nn_emp to contain empno,name,deptcode,desig,salary and insert some records(10)

 2. Create another table ai_nn_dept to contain dept_no(values match with deptcode of emp ),dept_name,dept_location and insert some records.
	(nn must be 01,02,03 etc. i.e. as per your username)
 3. Open ipython and import the necessary modules for data analysis

 4. load data from ai_nn_emp and ai_nn_dep into different dataframes 

 5. Print empno,name,deptname,salary and store the same to another dataframe in the ascending order of salary column.

 6. Write the above dataframe (after step5) into another table in mysql named ai_nn_emp_dept.


   (try 'mysql://ai:ai@127.0.0.1:3306/ai' as the parameter for create_engine of sqlalchemy)
         (dbms://user:password@hostname:portnumber/database)

"""

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
