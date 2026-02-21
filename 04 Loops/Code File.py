# Print numbers from 1 to 10 
for i in range(1,11):
    print(i)

# Print even numbers from 1 to 100
for i in range(1,101):
    if i % 2 == 0:
        print(i)

# Sum of first N natural numbers
a = int(input("Enter amount of number you want sum : "))
b = []
for i in range(1,a+1):
    b.append(i)
print(sum(b))
