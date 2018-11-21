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

f = open("emp.csv")

content = f.readlines()
elements = content[0].strip().split(',')


doc = dm.Document()


root = doc.createElement('root')

for c in content[1:]:
    datas = c.strip().split(',')
    emp = doc.createElement('employee')
    i=0
    for data in datas:
        child = doc.createElement(elements[i])
        child.appendChild(doc.createTextNode(data))
        emp.appendChild(child)    
        i +=1
    root.appendChild(emp)
    
doc.appendChild(root)

fd = open('employee.xml','w')

doc.writexml(fd)


