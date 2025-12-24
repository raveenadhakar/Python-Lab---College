# 1. WAP to Add Two Numbers
# (a) int + int
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
print("Sum =", a + b)

# (b) int + float
a = int(input("Enter integer: "))
b = float(input("Enter float: "))
print("Sum =", a + b)

# (c) float + float
a = float(input("Enter first float: "))
b = float(input("Enter second float: "))
print("Sum =", a + b)

# (d) str + str
a = input("Enter first string: ")
b = input("Enter second string: ")
print("Result =", a + b)

# 2. WAP to Check Even or Odd
n = int(input("Enter a number: "))

if n % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# 3. WAP to Calculate Compound Interest (CI)
p = float(input("Enter principal: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time: "))

ci = p * (1 + r/100) ** t
print("Compound Interest =", ci)

# 4. WAP to Find Largest Among Two Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest number is", a)
else:
    print("Largest number is", b)

# 5. WAP to Check Prime Number
n = int(input("Enter a number: "))

if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("Not a Prime Number")
            break
    else:
        print("Prime Number")
else:
    print("Not a Prime Number")



