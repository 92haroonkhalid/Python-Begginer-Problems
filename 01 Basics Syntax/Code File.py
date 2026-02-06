# Simple Print Statement
print("Hello World!")

# Print age, name, and city
age = 25
name = "Alice"
city = "New York"

print(f"Age: {age}")
print(f"Name: {name}")
print(f"City: {city}")

# Take user input and print it
x = input("Enter your number : ")
print(f"You entered: {x}")

# Add two numbers entered by user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

sum_ab = a + b
print(f"The sum of {a} and {b} is: {sum_ab}")

# Swap two variables
x = "Ali"
y = "Umair"

temp = x
x = y
y = temp

print(f"This is x : {x} and y : {y} after swapping. ")

# Check python version
import sys
print("Python version\n",sys.version)

# Print multiple lines using one print statement
print("Choose one option from below\n1.Yes\n2.No\n3.Maybe")

# Use comments to explain your code
# Already used to tell about each program 

# Assign multiple variables in one line
x,y,z = "Infront","Beside" ,"Behind"
print(x,y,z)

# Print data type of a variable
x = "Ali"
print(f"Types of x : {type(x)}")
