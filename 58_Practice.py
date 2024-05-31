# Program to convert Decimal to Binary using Recurssion

def ConvertBinary(n):
    if (n > 1):
        ConvertBinary(n // 2)
    print(n % 2, end='')

print('The binary of the given number is:- ')

ConvertBinary(15)