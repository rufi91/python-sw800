"""
Open python interpreter/ipython and do the following.
0.import pandas 
1.Using the emp.csv file available in common folder,create a data frame object named ef1.
2.Remove all the non digit characters from ephno column and store the new data in ef2. 
"""

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

#6.3.Display the lowest salary for scientist designation.
print ef4.loc['scientist'].min()['sal']
