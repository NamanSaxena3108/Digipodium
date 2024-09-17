#Write a program that creates an empty list and then asks the user to input integers to add to the list. Print the final list.
from typing import List

print("Program 1")
l = []
n = int(input("Enter the number of elements you want to add to the list: "))
for i in range(n):
  a = int(input("Enter the element:"))
  l.append(a)
print(l)

#Write a program that creates a list of integers and then asks the user to input an integer to check if it exists in the list. Print a message indicating whether the integer is in the list or not.
print("Program 2")
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = int(input("Enter the number you want to check: "))
if a in l:
  print("The number is in the list")
else:
  print("The number is not in the list")

#Write a program that creates a list of strings and then sorts the list alphabetically. Print the sorted list.
print("Program 3")
l = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
l.sort()
print(l)

#Write a program that creates a list of integers and then finds the maximum value in the list. Print the maximum value.
print("Program 4")
l = []
n = int(input("Enter the number of elements you want to add to the list: "))
for i in range(n):
  a = int(input("Enter the element:"))
  l.append(a)
print(l)
print("The maximum value in the list is:", max(l))

#Write a program that creates two lists of integers and then finds the common elements between those two lists. Print the common elements.
print("Program 5")
l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7, 8]
for i in l1:
  if i in l2:
    print(i)

#Write a program that creates a list of strings and then removes all elements that contain a specific substring. Print the final list.
print("Program 6")
l = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
a = input("Enter the substring you want to remove: ")
for i in l:
  if a in i:
    l.remove(i)
print(l)

#Write a program that creates a nested list and then accesses a specific element in the list. Print the accessed element.
print("Program 7")
l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(l[1][2])

#Write a program that creates a list of integers and then removes all duplicates from the list. Print the final list.
print("Program 8")
l = [1, 2, 3, 1, 5, 6, 2, 7, 9, 1, 4, 3, 5, 2, 4]
s = set(l)
l = list(s)
print(l)

#Write a program that creates a list of strings and then finds the longest string in the list. Print the longest string.
print("Program 9")
l = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
longest_string = l[0]
for i in l:
  if len(i) > len(longest_string):
    a = l.index(i)
    longest_string = l[a]
print(longest_string)

#Write a program that creates a list of integers and then finds the sum of all the even numbers in the list. Print the sum.
print("Program 10")
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s = 0
for i in l:
  if i % 2 == 0:
    s += i
print(s)

#Write a program that creates a list of integers and then asks the user to input a position to remove an element from the list. Print the final list.
print("Program 11")
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = int(input("Enter a index from which we have to remove the element: "))
if n < len(l):
  a = l.pop(n)
else:
  print("index out of bound")
print(l)

#Write a program that creates a list of strings and then concatenates all the strings into a single string. Print the final string.
print("Program 12")
l = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
new_string = ""
for i in l:
  new_string += i
print("string after concatination :", new_string)

#Write a program that creates a list of integers and then finds the median value of the list. Print the median.
print("Program 11")
l = [1, 10, 8, 2, 7, 3, 6, 4, 5, 9]
l.sort()
n = len(l) // 2
median = (l[n] + l[n - 1]) / 2
print(median)

#Write a program that creates a list of strings and then reverses the order of the strings in the list. Print the reversed list.
print("Program 12")
l = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
l2 = l[::-1]
print(l2)

#Write a program that creates a list of integers and then calculates the average of all the numbers in the list. Print the average.
print("Program 13")
l = [1, 10, 8, 2, 7, 3, 6, 4, 5, 9]
sum = 0
c = 0
for i in l:
  sum += i
  c += 1
print(f"Average is {sum/c}")

#Write a program that creates a list of integers and then finds the index of a specific element in the list. Print the index.
print("Program 14")
l = [1, 10, 8, 2, 7, 3, 6, 4, 5, 9]
n = int(input("Enter the number to search"))
if n in l:
  s = l.index(n)
print(f"Found the value at index {s}")

#Write a program that creates a list of strings and then removes all whitespace characters from each string in the list. Print the final list.
print("Program 15")
l = [
    "   apple    ", "   banana   ", "   cherry   ", " date   ",
    "   elderberry   ", "   fig   ", "   grape   "
]
l2 = [i.strip() for i in l]
print(l)
print(l2)

#Write a program that creates a list of integers and then sorts the list in descending order. Print the sorted list.
print("Program 16")
l = [1, 10, 8, 2, 7, 3, 6, 4, 5, 9]
l.sort(reverse=True)
print(l)

#Write a program that creates a list of integers and then asks the user to input a value to add to the list. Add the value to the beginning of the list and print the final list.
print("Program 17")
l = [1, 10, 8, 2, 7, 3, 6, 4, 5, 9]
n = int(input("Enter the number to add "))
l.insert(0, n)
print(l)

#Write a program that creates two lists of integers and then concatenates those two lists into a single list. Print the final list.
print("Program 18")
l1 = [1, 5, 6, 8, 1, 4]
l2 = [5, 9, 8, 2, 6, 3]
l1.extend(l2)
print(l1)

#Write a program that uses the map function to create a new list that contains the squares of each element in a user inputted list of integers.
print("Program 19")
n = int(input("Enter the no. of element"))
l = []
for i in range(n):
  a = int(input("Enter a number"))
  l.append(a)
l2 = list(map(lambda x: x**2, l))
print(l2)

#Write a program that uses a lambda expression and the map function to convert a list of integers to a list of strings. Print the new list.
print("Program 20")
n = int(input("Enter the no. of element"))
l = []
for i in range(n):
  a = int(input("Enter a number"))
  l.append(a)
l2 = list(map(lambda x: str(x), l))
print(l2)

#Write a program that uses a lambda expression and the map function to add 10 to each element in a list of integers. Print the new list.
print("Program 21")
n = int(input("Enter the no. of element"))
l = []
for i in range(n):
  a = int(input("Enter a number"))
  l.append(a)
l2 = list(map(lambda x: x + 10, l))
print(l2)

#Write a program that uses the map function to create a new list that contains the first letter of each string in a user inputted list of strings.
print("Program 22")
n = int(input("Enter the no. of element"))
l = []
for i in range(n):
  a = input("Enter the string ")
  l.append(a)
l2 = list(map(lambda x: x[0], l))
print(l2)

#Write a program that uses a lambda expression and the map function to convert a list of Celsius temperatures to a list of Fahrenheit temperatures. Print the new list.
print("Program 23")
n = int(input("Enter the no. of element"))
l = []
for i in range(n):
  a = int(input("Enter the temperature "))
  l.append(a)
l2 = list(map(lambda x: (9 / 5) * x + 32, l))
print(l2)

#Write a program that uses a lambda expression and the map function to convert a list of strings to a list of integers. Print the new list.
print("Program 24")
n = int(input("Enter the no. of element"))
l = []
for i in range(n):
  a = input("Enter the string ")
  l.append(a)
l2 = list(map(lambda x: int(x) if x.isdigit() else None, l))
print(l)
print(l2)

#Write a program that uses the map function to create a new list that contains the length of each string in a user inputted list of strings.
print("Program 25")
n = int(input("Enter the no. of element"))
l = []
for i in range(n):
  a = input("Enter the string ")
  l.append(a)
l2 = list(map(lambda x: len(i), l))
print(l)
print(l2)

#Write a program that uses a lambda expression and the map function to calculate the square root of each element in a list of integers. Print the new list.
print("Program 26")
import math

n = int(input("Enter the no. of element"))
l = []
for i in range(n):
  a = int(input("Enter a number"))
  l.append(a)
l2 = list(map(lambda x: round(math.sqrt(x), 2), l))
print(l2)

#Write a program that uses a lambda expression and the map function to convert a list of integers to their absolute values. Print the new list.
print("Program 27")
n = int(input("Enter the no. of element"))
l = []
for i in range(n):
  a = int(input("Enter a number"))
  l.append(a)
l2 = list(map(lambda x: abs(x), l))
print(l2)

#Write a program that uses the map function to create a new list that contains the uppercase version of each string in a user inputted list of strings.
print("Program 28")
n = int(input("Enter the no. of element"))
l = []
for i in range(n):
  a = input("Enter the string ")
  l.append(a)
l2 = list(map(lambda x: x.upper(), l))
print(l2)

#Write a program that uses the filter function to create a new list that contains only the even numbers from a user inputted list of integers.
print("Program 29")
n = int(input("Enter the no. of element"))
l = []
for i in range(n):
  a = int(input("Enter a number"))
  l.append(a)
l2 = list(map(lambda x: int(x) if x % 2 == 0 else " ", l))
print(l2)

#Write a program that uses a lambda expression and the filter function to create a new list that contains only the strings that start with a vowel from a user inputted list of strings.
print("Program 30")
n = int(input("Enter the no. of element"))
l = []
for i in range(n):
  a = input("Enter the string ")
  l.append(a)
l2 = list(filter(lambda x: x[0] in "aeiouAEIOU", l))
print(l2)

#Write a program that uses the filter function to create a new list that contains only the strings with a length greater than 5 from a user inputted list of strings.
print("Progrm 31")
n = int(input("Enter the no. of element"))
l = []
for i in range(n):
  a = input("Enter the string ")
  l.append(a)
l2 = list(filter(lambda x: len(x) > 5, l))
print(l2)

#Write a program that uses a lambda expression and the filter function to create a new list that contains only the positive numbers from a user inputted list of integers.
print("Program 32")
n = int(input("Enter the no. of element"))
l = []
for i in range(n):
  a = int(input("Enter a number"))
  l.append(a)
l2 = list(filter(lambda x: x > 0, l))
print(l2)

#Write a program that uses the filter function to create a new list that contains only the strings that contain the letter "e" from a user inputted list of strings.
print("Program 33")
n = int(input("Enter the no. of element"))
l = []
for i in range(n):
  a = input("Enter the string ")
  l.append(a)
l2 = list(filter(lambda x: x.count("e") > 0, l))
print(l2)

#Write a program that creates a nested list from two user inputted lists of integers. The resulting nested list should contain each element of the first list paired with the corresponding element of the second list.
print("Program 34")
n = int(input("Enter the no. of element"))
l = []
for i in range(n):
  a = int(input("Enter a number"))
  l.append(a)
l2 = []
for i in range(n):
  a = int(input("Enter a number"))
  l2.append(a)
l3 = list(zip(l1, l2))
print(l3)

#
