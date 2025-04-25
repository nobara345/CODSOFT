# Simple Calculator
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Select operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

op = input("Enter operation (1, 2, 3, 4): ")

if op == '1':
    print("Result:", a + b)
elif op == '2':
    print("Result:", a - b)
elif op == '3':
    print("Result:", a * b)
elif op == '4':
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Cannot divide by zero")
else:
    print("Invalid operation")
