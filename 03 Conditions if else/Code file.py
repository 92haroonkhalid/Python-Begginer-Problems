# Check if number is positive or negative
x = int(input("Enter a number : "))
if x > 0:
    print("It is a positive number.")
elif x < 0:
    print("It is a negative number.")
else:
    print("It is zero")

# Check even or odd
x = int(input("Enter a number : "))
if (x % 2 == 0):
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
x = int(input("Enter a year to check if it is a leap year or not :"))
if x % 4 != 0:
    print("It is a simple year not a leap year.")
else:
    print("It is a leap year.")

# Check voting eligibility
age = int(input("Enter your age in numbers : "))
if age >= 18:
    print("You are eligible to cast a vote in elections.")
else:
    print("Not eligible.")

# Check pass or fail
marks = int(input("Enter your marks in digits :"))
if marks >= 50:
    print("Congrats! You are passed.")
else:
    print("You are fail.")

# Convert marks to grade
marks = int(input("Enter your marks in digits : "))
if 85 <= marks <= 100:
    print("Grade A")
elif 75 <= marks < 85:
    print("Grade B+")
elif 70 <= marks < 75:
    print("Grade B")
elif 65 <= marks < 70:
    print("Grade C+")
elif 60 <= marks < 65:
    print("Grade C")
elif 55 <= marks < 60:
    print("Grade D+")
elif 50 <= marks < 55:
    print("Grade D")
else :
    print("Grade F")

# Check if character is vowel
a = input("Enter a character to check if it is vowel or not : ").lower()
if a in "aeiou":
    print("It is a vowel character.")
else:
    print("It is a consonent.")

# Simple calculator using if-else
n1 = int(input("Enter 1st number : "))
n2 = int(input("Enter 2nd number : "))
choice = int(input("Enter 1 to add, 2 to sub, 3 to mult, and 4 to div\n"))
if choice == 1:
    print(n1+n2)
elif choice == 2:
    print(n1-n2)
elif choice == 3:
    print(n1*n2)
elif choice == 4:
    print(n1/n2)
else:
    print("Invalid choice!")
