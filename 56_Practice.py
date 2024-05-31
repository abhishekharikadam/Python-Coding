# Program to find sum of natural numbers using recurssion

def NNS(n):
    if (n <= 1):
        return n
    else:
        return (n) + NNS(n - 1)

n = int(input("Enter a number:- "))

if (n <= 0):
    print("Enter a positive integer")
else:
    print("The sum of natural numbers upto given number is:-", NNS(n))