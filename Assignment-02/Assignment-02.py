'''   Assignment-02   '''

import keyword
import A1
from datetime import datetime

# 1. Write a python script to add comments and print “Learning Python” on screen.
# THIS IS SINGLE LINE COMMENT IN PYTHON
print("Learning Python")

# 2. Write a python script to add multi line comments and print values of four variables,each in a new line. Variable contains any values.
'''
THIS IS
MULTILINE COMMENT 
IN PYTHON
'''
var1, var2, var3, var4 = 123, 45.67, "String", 8+9j
print(var1, var2, var3, var4, sep='\n')

# 3. Write a python script to print types of variables. Create 5 variables each of them containing different types of data. (like 35, True, “MySirG”,5.46, 3+4j, etc)
var1, var2, var3, var4, var5 = 12, False, "MySirG", 34.5, 6+7j
print(type(var1), type(var2), type(var3), type(var4), type(var5), sep='\n')

# 4. Write a python script to print the id of two variables containing the same integer values.
num1, num2 = 12, 12
print(id(num1), id(num2))

# 5. Create four variables in a Python script and assign values of different data types to them. Write a Python script to print value, its type and id of each variable
var1, var2, var3, var4 = 12, 345.6, "This is String", True
print(var1, type(var1), id(var1))
print(var2, type(var2), id(var2))
print(var3, type(var3), id(var3))
print(var4, type(var4), id(var4))

# 6. Write a python script to print all the keywords
print(keyword.kwlist)

# 7. On Python shell use help() function and display the list of keywords

# 8. Create two Python files A0.py(in my case Assignment-02) and A1.py. Create a variable in A1.py and assign some value to it. Write a python script to import A1 module in A0 and print value of the variable created in A0.py
print("var1 =", A1.var1)

# 9. Name the keywords, used as data in the Python script.
'''
True
False
None 
'''

# 10. Write a python script to display the current date and time. First create variables to store date and time, then display date and time in proper format (like: 13-8-2022 and 9:00 PM)
currentDateTime = datetime.today()
currentDateTime = currentDateTime.strftime("%d-%m-%Y and %I:%M %p")
print(currentDateTime)
