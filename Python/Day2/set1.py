#!/bin/usr/env python
"""
#1
def oddoreven(num):
    if (num%2 == 0):
        print("Number is even")
    else:
        print("Number is odd")

for i in range(1,6):
    n=int(input("Enter a num: "))
    oddoreven(n)

#2

def greatest(a,b,c):
    if (a>b and a>c):
        print(a," is the greatest of all 3")
    if (b>a and b>c):
        print(b," is the greatest of all 3")
    if (c>a and c>b):
        print(c," is the greatest of all 3")

x=int(input("Enter first num: "))
y=int(input("Enter sec num: "))
z=int(input("Enter third num: "))
greatest(x,y,z)


#3

n=int(input("Enter a num: "))
if (n%2 == 0):
        print("Number is even")
else:
        print("Number is odd")


#4

def greatest():
    a=int(input("Enter first num: "))
    b=int(input("Enter sec num: "))
    c=int(input("Enter third num: "))
    if (a>b and a>c):
        print(a," is the greatest of all 3")
    if (b>a and b>c):
        print(b," is the greatest of all 3")
    if (c>a and c>b):
        print(c," is the greatest of all 3")


greatest()
"""

#6
name=input("Enter a name: ")
mark=input("Enter mark: ")
print ('%s scored %s of 100' % (name,mark))


