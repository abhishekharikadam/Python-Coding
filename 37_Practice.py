# Factorial solution using recurssion

def fact(a):
    if (a == 0):
        return 1
    else:
        return ((a) * fact(a - 1))
    
num = int(input("Enter a number here:- "))

result = fact(num)

print("The factorial of the given number is ", result)