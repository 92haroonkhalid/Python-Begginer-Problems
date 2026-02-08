# Create variables of all basic data types
x = None
y = "Ali"
z = 23
a = 5.4
b = True

# Convert int to float
x = 7
x = float(x)
print(x)

# Convert string to integer
x = int("123")
print(x)

# Check type of user input
x = input("Enter number : ")
print(type(x))

# Perform arithmetic operations
a = 3
b = 8
print(a+b)
print(a-b)
print(a*b)

# Calculate area of a rectangle
length = 10
width = 6
print("Area of rectangle is : ", length*width)

# Calculate simple interest
princple_amount = 500
interest = 200
interest_rate = 6
print("Simple Interest is : ", (princple_amount*interest*interest_rate)/100)

# Store and print boolean values
x = True
y = False
print(x , y)

# Use type() function
x = 5
print(type(x))

# Take input and display its length
x = input("Enter something : ")
print("Length of entered string is : ",len(x))
