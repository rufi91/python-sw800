"""
1. Create a csv file emp.csv that contains the following data,
    eno,ename,edesig,esalary
    101,Anil,scientist,50000
    102,Mary,scieltist,55000
    103,Raju,engineer,60000
    104,Ravi,officer,40000
   write a script to create an xml file from the above data.
   (employee can be made as root node)
   """

import xml.dom.minidom as dm
import pandas as pd

text= pd.read_csv('emp1.csv', delimiter='\t')
text= text.as_matrix()
doc=dm.Document()
e1=doc.createElement('employee')


for i in range(0,text.shape[0]):
    
    e11=doc.createElement('eno')
    e12=doc.createElement('ename')
    e13=doc.createElement('edesig')
    e14=doc.createElement('esalary')
    print text[i][0]

    t11=doc.createTextNode(str(text[i][0]))
    t12=doc.createTextNode(str(text[i][1]))
    t13=doc.createTextNode(str(text[i][2]))
    t14=doc.createTextNode(str(text[i][3]))

    e11.appendChild(t11)
    e12.appendChild(t12)
    e13.appendChild(t13)
    e14.appendChild(t14)

    e1.appendChild(e11)
    e1.appendChild(e12)
    e1.appendChild(e13)
    e1.appendChild(e14)
    doc.appendChild(e1)


fd=open('empresult.xml','w')
doc.writexml(fd, newl='\n', indent='\t', addindent='\t')
