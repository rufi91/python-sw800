"""
1. Write a script to print numbers in descending order starting 
	from a given input(do not use a loop).
2. Do 1 using while loop.
3. Write a script to print factorial of a number (without using loop).
4. Do 3 using while loop
5. Write a script to check whether an input number is prime or not.
   (use while loop without else)



#1
def desc(n):
        if n >= 1:
            print (n)
            desc(n-1)

num=int(input("enter no :"))
desc(num)

#2

n=int(input("enter no :"))
while n >= 1:
    print(n)
    n-=1

#3,4

n=int(input("enter no :"))
fact=n
while n > 1:
    fact=fact*(n-1)
    n-=1
print(fact)
 """  
#5
n=int(input("enter no :"))
i=2
prime=1
while (i <= n/2):
    if n%i == 0:
        prime=0
        print("no not prime")
        break
    i+=1

if(prime==1):
    print("no is prime")

   
        

    
    
