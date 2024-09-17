#Write a program to print numbers from 1 to 10 using a for loop.
print("Program 1")
for i in range(1,11):
  print(i)
  
#Write a program to print the multiplication table of a given number using a while loop.
print("Program 2")
num=int(input("Enter a number \n"))
i=1
while i<=10:
  print(f"{num}*{i}={num*i}")
  i+=1
  
#Write a program to find the sum of all even numbers between 1 and 100 using a for loop.
print("Program 3")
sum=0
for i in range(1,101):
  if i%2==0:
    sum += i
print(sum,"\n")

#Write a program to check if a given number is prime or not using a while loop.
print("Program 4")
num=int(input("Enter a number \n"))
i=2
while i<num:
  if num %i==0:
    print(f"{num} is not a prime number")
    break
  i+=1
else:
  print(f"{num} is a prime number")

#Write a program to calculate the factorial of a number using a for loop.
print("Program 5")
num=int(input("Enter a number \n"))
fact=1
for i in range(1,num+1):
  fact*=i
print(fact)

#Write a program to print the Fibonacci series up to a given limit using a for loop.
print("Program 6")
limit=int(input("Enter a limit \n"))
a=0
b=1
print(a)
print(b)
for i in range(1,limit+1):
  c=a+b
  print(c)
  a=b
  b=c

#Write a program to find the largest element in an array using a for loop.
print("Program 7")
l1=[1,2,3,4,5,6,7,8,9,10]
largest=l1[0]
for i in l1:
  if i>largest:
    largest=i
print(f"Largest element in the list is {largest}")

#Write a program to reverse a given string using a while loop.
print("Program 8")
str=input("Enter a string \n")
i=len(str)-1
rev=""
while i>=0:
  rev+=str[i]
  i-=1
print(rev)

#Write a program to print the ASCII values of all uppercase letters using a for loop.
print("Program 9")
for i in range(65,91):
  print(chr(i),end=" ")
print("\n")

#Write a program to check if a given string is a palindrome using a for loop.
print("Program 10")
str=input("Enter a string \n")
i=0
j=len(str)-1
flag=True
while i<j:
  if str[i]!=str[j]:
    flag=False
    break
  i+=1
  j-=1
if flag:
  print("Palindrome")
else:
  print("Not a palindrome")

#Write a program to calculate the average of a list of numbers using a for loop.
print("Program 11")
l1=[1,2,3,4,5,6,7,8,9,10]
sum=0
c=0
for i in l1:
  sum+=i
  c+=1
print(sum/c)

#Write a program to find the smallest element in an array using a while loop.
print("Program 12")
l1=[1,2,3,4,5,6,7,8,9,10]
smallest=l1[0]
i=1
while i<len(l1):
  if l1[i]<smallest:
    smallest=l1[i]
  i+=1
print(f"Smallest element in the list is {smallest}")

#Write a program to calculate the sum of digits of a number using a for loop.
print("Program 13")
num=int(input("Enter a number \n"))
sum=0
while num>0:
  sum+=num%10
  num=num//10
print(sum)

#Write a program to check if a given list of years has a leap year using a while loop.
print("Program 14")
l1=[2000,2001,2002,2003,2004,2005,2006,2007,2008,2009
    ,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019
    ,2020,2021,2022,2023,2024]
i=0
while i<len(l1):
  if (l1[i]%4==0 and l1[i]%100!=0) or (l1[i]%400==0):
    print(f"{l1[i]} is a leap year")
  i+=1

#Write a program to print the multiplication table of numbers from 1 to 5 using a for loop.
print("Program 15")
for i in range(1,6):
  for j in range(1,11):
    print(f"{i}*{j}={i*j}")
  print()

#Write a program to find the factorial of a number using a for loop.
print("Program 16")
print("Done above in program 5 \n")

#Write a program to count the number of vowels in a given string using a for loop.
print("Program 17")
str=input("Enter a string \n").lower()
vowels="aeiou"
c=0
for i in str:
  if i in vowels:
    c+=1
print(c)

#Write a program to find the largest and smallest elements in an array using a for loop.
print("Program 18")
l1=[1,2,3,4,5,6,7,8,9,10]
smallest=l1[0]
i=1
while i<len(l1):
  if l1[i]<smallest:
    smallest=l1[i]
  i+=1
print(f"Smallest element in the list is {smallest}")
largest=l1[0]
for i in l1:
  if i>largest:
    largest=i
print(f"Largest element in the list is {largest}")

#Write a program to reverse the order of words in a sentence using a while loop.
print("Program 19")
str=input("Enter a string \n")
i=len(str)-1
rev=""
while i>=0:
  rev+=str[i]
  i-=1
print(rev)

