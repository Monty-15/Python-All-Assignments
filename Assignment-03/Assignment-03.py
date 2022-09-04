'''   Assignment-03   '''

# 1. Write a python script to convert a number into str type.
num1 = 12
str1 = str(num1)
print(type(str1))

# 2. Write a python script to print Unicode of the character ‘m’
print(ord('m'))

# 3. Write a python script to print character representation of a given unicode 100.
print(chr(100))

# 4. Write a python script to print any number and its binary equivalent
num1 = 154
print(num1, bin(num1), sep='\n')

# 5. Write a python script to print any number and its octal equivalent.
num1 = 524
print(num1, oct(num1), sep='\n')

# 6. Write a python script to print any number and its hexadecimal equivalent.
num1 = 15
print(num1, hex(num1), sep='\n')

# 7. Write a python script to store binary number 1100101 in a variable and print it in decimal format.
num1 = 0b11001101
print(num1)

# 8. Write a python script to store a hexadecimal number 2F in a variable and print it in octal format.
num1 = 0x2F
print(oct(num1), sep='\n')

# 9. Write a python script to store an octal number 125 in a variable and print it in binary format.
num1 = 0o125
print(bin(num1))

# 10. Write a python script to add two numbers 25 (in octal) and 39 (in hexadecimal) and display the result in binary format.
num1 = 0o25
num2 = 0x39
sum = bin((int(str(oct(num1)), 8))+(int(str(hex(num2)), 16)))
print(sum)
