#Create a string and print it.
print("Program 1")
print("Hello World")

#Take a string input and print it's length
print("Program 2")
str=input("Enter a string: ")
print("The length of the string is: ",len(str))

#Print the last word of the string Python is great using slices.
print("Progam 3")
str="Python is great"
print(str[9:])

#Print the each word in different line of string python is everywhere.
print("Program 4")
str="Python is everywhere"
print(str[0:6])
print(str[7:9])
print(str[10:])

#Print the string Hello World! in reverse.
print("Program 5")
str="Hello World!"
print(str[::-1])

#Convert the string How are you? in uppercase.
print("Program 6")
str="How are you?"
print(str.upper())

#Convert the string How Is It Going? in lowercase.
print("Program 7")
str="How Is It Going?"
print(str.lower())

'''Join the following list by spaces( ) and print the result.
words = ['Python', 'is', 'easy', 'to', 'learn']'''
print("Program 8")
words = ['Python', 'is', 'easy', 'to', 'learn']
print(" ".join(words))

#Print a multiline string using a single print
print("""Program 9
Hello
World
!""")

#Print this string to move to newline '\n' is used. (results should look exactly like the provided string)
print("Program 10")
print(r"Print this string to move to newline '\n' is used.")

'''Print a variable with some text using a single print function, output should look like following.
the variable is 15'''
print("Program 11")
var=15
print(f"the variable is {var}")

'''concatenate the following strings and print the result
s1 = 'python '
s2 = 'is '
s3 = 'great.'
'''
print("Program 12")
s1 = 'python '
s2 = 'is '
s3 = 'great.'
print(s1+s2+s3)

#Print # 20 times without using a loop
print("Program 13")
print("#"*20)

'''Print numbers from 1 to 9, each on a seperate line, followed by a dot, output should look like the following-
1.
2.
3.'''
print("Program 14")
for i in range(1,10):
  print(f"{i}.")

#Ask user to input a sentence and print each word on a different line.
print("Program 15")
str=input("Enter a sentence: ")
new_str=str.split()
for i in new_str:
  print(i)

#Ask user to input a string and check if the string ends with '?'
print("Program 16")
str=input("Enter a string: ")
if str.endswith("?"):
  print("It ends with ?")
else:
  print("It does not end with ?")

#Ask user to input a string and print how many times e appeared in the string
print("Program 17")
str=input("Enter a string: ")
print("E has appeared",str.count("e"),"times")

#Check if the user input is a number.
print("Program 18")
str=input("Enter a string: ")
if str.isdigit():
  print("It is a number")
else:
  print("It is not a number")

'''Remove the extra spaces in beginning and in the end of the following string-
text = '   this is not a good string           '
'''
print("Program 19")
text = '   this is not a good string           '
print(text.strip())

#Ask user to input string, print found if any of the character is upper case.
print("Program 20")
str=input("Enter a string: ")
if str.islower():
  print("It is all lower case")
else:
  print("It is not all lower case")

'''Extract names from the following string and store them in a list.
names = 'Joe, David, Mark, Tom, Chris, Robert'
'''
print("Program 21")
names = 'Joe, David, Mark, Tom, Chris, Robert'
print(names.split(","))  

'''In the following string, add aye in the end of every word and print the results.
text = 'this is some text'
'''
print("Program 22")
text = 'this is some text'
print(text.replace(" ", "aye "))

#ask user to enter a string and check if the string contains fyi
print("Program 23")
str=input("Enter a string: ")
if "fyi" in str:
  print("It contains fyi")
else:
  print("It does not contain fyi")

'''Remove all the special characters and numbers from the following string
text = '%p34@y!*-*!t68h#&on404'4
'''
print("Program 24")
text = '%p34@y!*-*!t68h#&on404'
for i in text:
  if i.isalnum():
    print(i,end="")

'''calculate the average word length of the following paragraph.
this is a paragraph which is written just for the purpose of providing content to let the average word length be calculated'''
print("Program 25")
text = 'this is a paragraph which is written just for the purpose of providing content to let the average word length be calculated'
new_text=text.split()
sum=0
for i in new_text:
  sum=sum+len(i)
print("The average word length is",int(sum/len(new_text)))