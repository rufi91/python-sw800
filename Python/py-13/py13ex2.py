"""
 Write a script to create a table in mysql database using the data of emp.csv

   (table names can be chosen as emp_ai01,emp_ai02 etc for users AI01,AI02 etc)
   """

import MySQLdb as db
import pandas as pd

text= pd.read_csv('emp1.csv', delimiter='\t')
text= text.as_matrix()

try:
    con=db.connect('127.0.0.1','ai','ai','ai')
    cur=con.cursor()

    qstring1="""
    create table emp_ai21 (eno int, ename varchar(20), edesig varchar(20),
    esalary int)
    """
    #cur.execute(qstring1)

    for i in range(text.shape[0]):
        
       qstring2='insert into emp_ai21 values(%d, \'%s\', \'%s\', %d)' % (text[i][0],text[i][1],text[i][2],text[i][3])
       print qstring2
       cur.execute(qstring2)
       con.commit()

except Exception, arg:
    print "Exception occurd"
    print arg

finally:
    con.close()



#res=cur.fetchall()

