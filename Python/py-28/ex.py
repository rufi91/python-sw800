"""
2.Create a plot with different linestyle,color and marker for ,say, numbers less than 
50 and greater than or equal to 50 for an array of 10 random integers between 1 and 100
		
steps
1. import pyplot and numpy
2. create figure 
3. add a subplot
4. create and store 10 random integers between 1 and 100 in y array
5. split the array into two y1 and y2. hint:less than 50 in y1 ,others in y2,boolen indexing 
6. store last element of y1 as first in y2: hint numpy.insert(array,index,value)
7. create 10 even numbers in x array hint arange
7. call plot of step3 return value by supplying x array containg index values 0 thru size of y1
8. again call plot of step3 return value by supplying the required values
9. show the figure
		 	
"""
import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure(figsize=(6,6), facecolor='0.8')
sb1=fig.add_subplot(1,1,1)
y= np.random.randint(1,100,10)
y1=y[y<50]
y2= y[y>=50]
x= np.arange(2,21,2)
print y,'\n',y1,'\n',y2,'\n',x
print y1[-1]
y2=np.insert(y2,0,y1[-1])
print y2
sb1.plot(x[0:y1.size],y1,'ro:')
sb1.plot(x[y1.size-1:],y2,'bo--')
sb1.set_title("MATPLOTLIB")
sb1.set_xlabel("X AXIS")
sb1.set_ylabel("Y AXIS")
plt.show()
