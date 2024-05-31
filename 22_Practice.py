num1 = float(input("Enter the first number:- "))
num2 = float(input("Enter the second number:- "))

operation = str(input("Enter the operation (+, -, *, /): "))

if operation == '+':
    print(num1 + num2)
elif operation == '-':
    print(num1 - num2)
elif operation == '*':
    print(num1 * num2)
elif operation == '/':
    print(num1 / num2)
else:
    print("Invalid input")
    exit()