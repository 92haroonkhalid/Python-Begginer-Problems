# Check if number is positive or negative
x = int(input("Enter a number : "))
if x >= 0:
    print("It is a positive number.")
elif x < 0:
    print("It is a negative number.")

# Check even or odd
x = int(input("Enter a number : "))
if (x % 2 == 0 or x % 3 == 0):
    print("It is an Even number.")
else:
    print("Is is an Odd number.")

# Find largest of two numbers
a = int(input("Enter first number : "))
b = int(input("Enter secnd number : "))
if a>b:
    print(f"Given number {a} is greater than {b}")
elif a == b:
    print("Both are equal.")
else:
    print(f"Given number {b} is greater than {a}")

# Find largest of three numbers
a = int(input("Enter first number : "))
b = int(input("Enter secnd number : "))
c = int(input("Enter third number : "))
if a>b and a>c:
    print(f"{a} is greater than others.")
elif b>a and b>c:
    print(f"{b} is greater than others.")
elif a==b and a>c:
    print(f"Both {a} and {b} are equal and greater than {c}.")
elif c==b and a<c:
    print(f"Both {b} and {c} are equal and greater than {a}.")
else:
    print(f"{c} is greater than others.")

# Check if a year is leap year
x = int(input("Enter total days in year to check if it is a leap year or not :"))
if x==365:
    print("It is a simple year not a leap year.")
elif x==366:
    print("It is a leap year.")
else:
    print("Enter valid days.")
