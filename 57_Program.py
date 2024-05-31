# Program to find factorial using recurssion

def fact(n):
    if (n == 1):
        return 1
    else:
        return (n * fact(n - 1))
    
n = int(input("Enter the number:- "))
if (n < 1):
    print("The factorial of given number does not exist")
else:
    print('The factorial of given number is ', fact(n))