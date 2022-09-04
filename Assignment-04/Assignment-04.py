'''   Assignment-04   '''

# 1. Write a python script to take your name as input from the user and then print it.
myName = input("Input your name: ")
print("Your Name is", myName)

# 2. Write a python script to take input from the user. Input must be a number.
num1 = int(input("Input a number: "))
print("Your Inputed Number Is", num1)

# 3. Write a python script which takes two numbers from the user, then calculate their sum and display the result.
num1 = int(input("Input first number: "))
num2 = int(input("Input second number: "))
sum = num1 + num2
print(num1, "+", num2, "=", sum)

# 4. Write a python script which takes the radius from the user and display area of a circle.
radius = float(input("Input the value of radius: "))
areaOfCircle = 3.14 * radius * radius
print(areaOfCircle)

# 5. Write a python script to calculate the square of a number. Number is entered by the user.
num1 = int(input("Input a number: "))
print("Square of", num1, "is", num1*num1)

# 6. Write a python script to calculate the area of Triangle. Number is entered by the user.
baseOfTriangle = int(input("Input the value of base: "))
heightOfTriangle = int(input("Input the value of height: "))
areaOfTriangle = 1/2 * baseOfTriangle * heightOfTriangle
print(areaOfTriangle)

# 7. Write a python script to calculate average of three numbers, entered by the user
print("Input three number:")
num1, num2, num3 = float(input()), float(input()), float(input())
average = (num1+num2+num3)/3
print("Average is", average)

# 8. Write a python script to calculate simple interest
print("Input all information")
principal = float(input("Input intial principal balance: "))
rate = float(input("Input annual interest rate: "))
time = float(input("Input time(in year): "))
simpleInterest = (principal*rate*time)/100
print(simpleInterest)

# 9. Write a python script to calculate the volume of a cuboid.
length = float(input("Input length: "))
width = float(input("Input width: "))
height = float(input("Input height: "))
volumeOfCuboid = length*width*height
print(volumeOfCuboid)

# 10. Write a python script to calculate area of a rectangle
length = float(input("Input length: "))
width = float(input("Input width: "))
areaOfRectangle = length*width
print(areaOfRectangle)
