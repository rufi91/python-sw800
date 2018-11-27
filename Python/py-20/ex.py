"""
1 Create a numpy structured array using the emp.csv file available in common folder.
1.1 display all the records.
1.2 display names of officers.
1.3 display all the scientists records.
1.4 display the total salary.
1.5 display average salary of engineers.
1.6 display employees in the ascending order of salary.
1.7 display employees in the ascending order of designation and then salary.
1.8 display the lowest salary for scientist designation.
1.9 display records of employees who are scientists and are drawing the lowest salary(without using sort).
"""

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
