
"""
Day3
1. write a program to print the length of a string (without using len() function) using for loop.

2. Write a program to reverse a given string.

3. Write a program to print the no. of occurences of a given character in a given string.

4. Write a program to check for at least two vowels in a given string.
"""

#!/bin/usr/env python

#1
strlen=0
string = input ("Enter a string ")
for c in string:
    strlen+=1

print(strlen)

#2

string = input ("Enter a string ")
print(string[::-1])

#3
count=0
string = input ("Enter a string ")
char =input ("Enter a char ")
for c in string:
    if c==char:
        count+=1

print(count)

#4

count=0
string = input ("Enter a string ")
for c in string:
    if c in ('a','A','e','E','i','I','o','O','u','U'):
        count+=1
        if count==2:
            print('string has at least %d vowels' % (count))
            break
print(count)


