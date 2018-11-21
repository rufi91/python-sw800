"""
Copy emp.csv from common/python_exercises directory
Write  python scripts(use re module) to do the following
1.Write records that correspond to scientists to another file named sci.csv
2.Write records with single letter initials at the begining of the name to ini1.csv  
3.Write records with single letter initials anywhere in the name to ini2.csv
4.Write names and phone numbers to empphno.csv,remove extra characters from phno field.
5.write records with id greater than 200 to anotherfile named emp2.csv. 

#1
import re
f1= open('emp.csv','r')
f2= open('sci.csv','w')
file1=f1.readlines()
for line in file1:
    obj=re.search("scientist", line)
    if obj:
        #print line
        f2.writelines(line)

#2 with single letter initials at the begining of the name to ini1.csv
import re
f1= open('emp.csv','r')
f2= open('inil.csv','w')
file1=f1.readlines()
for line in file1:
    obj=re.match('([A-Z]\\.)',line.split(',')[0])
    if obj:
        print line
        f2.writelines(line)

#3single letter initials anywhere in the name to ini2.csv

import re
f1= open('emp.csv','r')
f2= open('inil2.csv','w')
file1=f1.readlines()
for line in file1:
    obj=re.match('.*([A-Z]\\..*)',line.split(',')[0])
    if obj:
        print line
        f2.writelines(line)

#4names and phone numbers to empphno.csv,remove extra characters from phno field.

import re
text=''
f1= open('emp.csv','r')
f2= open('empphno.csv','w')
file1=f1.readlines()
for line in file1:
    phno=re.sub('[^0-9]','',line.split(',')[4])
    text+=line.split(',')[0]+","+phno+"\n"

print text
f2.writelines(text)
   """ 
#5id greater than 200 to anotherfile named emp2.csv

import re
text=''
f1= open('emp.csv','r')
f2= open('emp2.csv','w')
file1=f1.readlines()
for line in file1:
    empid=line.split(',')[1]
    if(int(empid)>200):
        print line
        f2.writelines(line)

        
