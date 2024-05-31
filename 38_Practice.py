# Program to print multiplication table using for loop

num = int(input("Enter a number here:- "))

for i in range(1, 11):
    print(num, 'X', i, "=", num * i)