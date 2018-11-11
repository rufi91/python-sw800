
"""
Day 4
1. Write a script to reverse a given sentence without reversing words.
     
2. Write a script to print the no. of palindrome words in a given sentence.

3. Write a script to count letters in a given string(using dict).

4. Write a script to count words in a given sentence (using dict).


#1
strlen=0
rev=''
string = input ("Enter a string ")
word_list= string.split()
rev1 = word_list[::-1]
for words in rev1:
    rev=rev+words+" "

print(rev)

#2

count=0
string = input ("Enter a string ")
word_list= string.split()

for word in word_list:
    if word[::-1]== word:
        count+=1

print('Total number of palindrome words: ',count)
"""


