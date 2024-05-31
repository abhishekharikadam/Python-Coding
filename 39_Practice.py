# Pragram to print multiplication table using while loop

num = int(input("Enter a number here:- "))

i = 1

while i <= 10:
    print(num, 'X', i, "=", num * i)
    i = i + 1