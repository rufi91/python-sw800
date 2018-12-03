"""
A.Write a menu based python script to create a numpy structured array using the given(common folder) emp.csv file
    with the following options,

	a)initialize b)add new record c)delete a record d)Display details by name e)Display summary f)Save All g)Exit 

        a-Load data from emp.csv to numpy array
        b-Get details from user and append it to the existing numpy array
	c-Remove an employee record by receiving employee number
        d-Display an employee record by receiving ename or employee number
        e-Display total number of emplyees and total salary
        f-Replace emp.csv with the modified array
        g-Quit the program   
 """
import numpy as np



def emp_menu():
    global datatype
    global filedata
    print """=============EMPLOYEE CRUD PLATFORM=============\n\n

   
    1)initialize \n
    2)add new record \n
    3)delete a record \n
    4)Display details by name or eno\n
    5)Display summary \n
    6)Save All \n
    7)Exit """

    ip=input("\n Select an option: ")
  
    if(ip==1):     
    #initialize
        datatype= np.dtype([('ename','S20'),('eno','i8'),('edesig','S20'),('esal','f8'),('ephn','S20')])
        filedata = np.loadtxt('emp.csv', delimiter=',', dtype= datatype)
        print "\n Initialized data: \n", filedata
        emp_menu()
        
    if(ip==2):
    #add new record
        iname=raw_input("\n Enter Name: ")
        ino=input("\n Enter EmpNo: ")
        idesig=raw_input("\n Enter Designation: ")
        isal=input("\n Enter Salary: ")
        ipno=raw_input("\n Enter PhNo: ")
        inputdata=np.array([(iname, ino, idesig, isal,ipno)], dtype=datatype)
        print filedata.shape, inputdata.shape
        print inputdata
        filedata=np.concatenate([filedata,inputdata], axis=0)
        print filedata
        emp_menu()

    if(ip==3):
    #delete a record
        ino=input("\n Enter EmpNo to delete: ")
        filedata= filedata[(filedata['eno']!=ino)]
        print filedata
        emp_menu()
        
    if(ip==4):
    #display details by name or eno
        ip4=raw_input("\n Enter Detail: ")
        #filedata[(filedata['ename']==ip4 )              ]
        #filedata[(filedata['eno']==ip4 )]
        #data= filedata[(filedata['ename']==str(ip4) | filedata['eno']==int(ip4))]
        #print data
        emp_menu()

    if(ip==5):
    #display summary
        print "----------SUMMARY----------- \n"
        print "\n Total number of employees: ", len(filedata)
        print "\n Total salary: ", filedata['esal'].sum()
        emp_menu()

    if(ip==6):
    #save all to emp.csv
        print filedata
        np.savetxt('emp.csv', filedata, delimiter=',', fmt='%s')
        emp_menu()

    if(ip==7):
        exit()






emp_menu()
