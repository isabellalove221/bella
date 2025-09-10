
#--- Variables and Data Types ---
a = 5
print(a) # a is an integer, a whole number 
print(type(a))
b = 1.5
print(b)
print(type(b)) # b is a float, a number with decimals
c = 3j
print(c)
print(type(c)) # c is a complex, a number and a letter
d = "hello"
print(d)
print(type(d)) # d is a string, a word
e = [1, 2, 3]
print(e)
print(type(e)) # e is a list, a list of numbers
f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # f is a dictionary, a collection of values
g = (1, 2)
print(g)
print(type(g)) # g is a tuple, ordered list of items
h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # h is a list, a list of items 
i = True
print(i)
print(type(i)) # i is a boolean, a data type that has the values True and False
j = None
print (j)
print(type(j)) # j is None Type, meaning nothing is here
k = [True, "blue", 12]
print(k)
print(type(k)) # k is a list, a list of items 
l = str(14)
print(l)
print(type(l)) # l is a string
m = 1e4
print(m)
print(type(m)) # m is a float, a number with other characters 
# 1. How many different data types did you find?

# 2. List all the data types you found. integer, float, complex, string, list, dictionary, tuple, boolean, None Type
# 3. What variables have the same data types? d and l, m and b, h and k
# 4. What was the data type of l? Why is it not an integer? What does str() do? str() makes the integer a string instead 
# 5. Look up one more data type not given above. Repeat the same procedure.

n = b"Hello"
print(n)
print(type(n))

# --- Booleans ---
print(10>9) # true, 10 is greater than 9
print(10==9) # false, 10 is not equal to 9
print(10<=9) # false, 10 is not less than or equal to 9
print(bool("abc")) #true, abc is the correct order
print(bool(123)) #true, 123 is the correct order
print(bool(["apple", "cherry", "banana"])) #true, all fruits
print(bool(True)) #true, the input is true
print(bool(False)) #false, the input is false
print(bool(0)) #false, 0 values are false
print(bool("")) #false, no value is false
print(bool(" ")) #true, space is value 
print(bool(())) #false, no value
print(bool([])) #false, no value
print(bool({})) #false, no value
print(bool(True and False)) #false, one value is false
print(bool(True and True)) #true, values are both true
print(bool(False and False)) # false, both values are false
print(bool(True or False)) # true, at least one value is true 
print(bool(True or True)) #true, at least one value is true
print(bool(False or False)) #true, both values are false
print(bool(not(False))) #true, opposite of false
print(bool(not(True))) #false, opposite of true 
# What pattern do you notice about expressions returning True or False? with "and" the whole expression is only true if both sides are true, with "or" expression is true if one side is true, "not" is opposite
# Which expression surprised you about its result? a space makes the empty expression true
# Create an expression, not given above, that will return True. Why is it True?
print(bool(0 or 5)) #true since 1 side is true with "or"
# Create an expression, not given above, that will return False. Why is it False?
print(bool(4==4 and 10<5)) # false since 1 side is false with "and"

# ---Operators---
# arithmetic operators   
print(10+5) # 15, + performs addition
print(10-5) # 5, - performs subtraction
print(2*4) # 8, * performs multiplication
print(6/3) #2.0, / performs division
print(5%2) # 1.0, % gives the remainder of a/b (5/2), modulus
print(3**2) # 9, ** gives a to the power of b
print(15//2) # 7, // gives the nearest whole number
# comparison operators 
print(5 == 2) #false, == means equal to
print(10 != 10) #false, =! means not equal to
print(2<5) # true, < means less than
print(12>5) # true, > means greater than
print(5<=6) #, <= means less than OR equal to
print(1>=10) # false, >= means greater than or equal to
 # assignments operators 
x=5
x += 5 
print(x) # 10, x + 5 = 10
x -= 4
print(x) # 6, last x - 4 
x *= 3
print(x) # 18, last x * 3
# logical operators
# # 1. What does the operator and do? Write an expression that results in True. Write an expression that results in False. and returns true if both sides are true, otherwise it is false
print(5 > 2 and 3 < 4) # true, both sides are true
print(10==5 and 2<8) # false, first expression is false 
# 2. What does the operator or do? Write an expression that results in True. Write an expression that results in False. or returns true if at least one condition is true
print(5>10 or 7==7) # true, 7==7 is true
print(2>5 or 3<1) # both expressions are false
# 3. What does the operator not do? Write an expression that results in True. Write an expression that results in False. not outputs the opposite of a Boolean value
print(not False) # true, not false
print(not True) # false, not true
# 1. What is the difference between / and //? / gives the exact value, // rounds to a whole number
# 2. What is the difference between % and //? % gives the remainder after division, // gives the quotient without a remainder
# 3. What operator would you use to calculate the remainder when dividing two numbers? Give an example. # use %
print(15%4) # 3, 15/4= 12+3
# 4. How do assignment operators work? Assignment operators change the value of a variable by combining it with another value

# --- Strings ---
my_string = "hello"
print(my_string) # prints: hello 
print(my_string[0]) # prints: h
print(my_string[1]) # prints: e
print(my_string[2]) # prints: l
print(my_string[3]) # prints: l 
print(my_string[4]) # prints: o
print(my_string[-1]) # prints: o
print(my_string[1:3]) # prints: el
print(my_string[0:5:2]) # prints: hlo
print(len(my_string)) # prints: 5
print(my_string+" goodbye") # prints: hello goodbye
print(my_string*7) # prints: hellohellohellohellohellohellohello
# 1. Define the term slicing. For which of the manipulations did you slice your string? slicing means to take a portion of a string 
# 2. Call the following, describe the result: 
name = "Oski" 
print("Hello, my name is", name) # prints: Hello, my name is Oski
# 3. Call the following, describe the result. 
name = "Oski" 
print(f"Hello, my name is {name}") # prints: Hello, my name is Oski
# 4. What is the difference between the two last print statements? f string can perform more complex operations than the regular print function

# ---Terminal Commands---

# cd 
# change directories 
# cd python_decal_fa25/bella/

# ls
# list (shows folders in a directory)
# ls 

# ls -a 
# "list all" (shows all folders, even hidden)
# ls -a

# mkdir
# make directory 
# mkdir homework1

# cat 
# concatenate (shows contents of a file in terminal)
# cat homework1

# pwd 
# print working directory (shows full folder path)
# pwd 

# cd..
# change directory up one level (moves you to parent folder)
# cd..

#cd . 
# change directory to current 
# cd . 

#cd ~ 
# change directory to home folder
# cd ~

# cp
# copy
# copy file.txt backup.txt

# mv
# moves or renames folders
# mv notes.txt archive/

# rm
# removes/deletes files 
# rm homework1 

# clear
# clear screen, wipes terminal window 
# clear

# grep 
# global regular expression print, searches for text inside files
# grep "error" python_decal_fa25

# Look up 3 other commands not present. Define and explain how to use them on the command line.

# touch 
# creates new empty file
# touch homework1

# head 
# displays the first few lines of a file
# head homework1

# tail 
# displays the last few lines of a file 
# tail homework1

# 2. What is the difference between ls and ls -a? ls shows only visible folders, ls -a shows all folders including hidden ones
# 3. What is a hidden file? file that begins with a . they are hidden to avoid clutter but still accessible 
# 4. Look up 3 other flags (e.g., -a was a flag for the ls command). Define and explain how to use them on the command line

# ls -l
# lists files in long formal (with permissions, owner, size, and date)

# ls -h 
# "human readable" sizes, shows files in kb, mb

# ls -R
# lists files showing contents of sub directories too



