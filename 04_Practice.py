h1 = int(input("Enter the 1st number: "))
h2 = int(input("Enter the 2nd number: "))
h3 = int(input("Enter the 3rd number: "))
h4 = int(input("Enter the 4th number: "))

if (h1 > h2):
    f1 = h1
else:
    f1 = h2

if (h3 > h4):
    f2 = h3
else:
    f2 = h4

if (f1 > f2):
    print(str(f1) + " is greater")
else:
    print(str(f2) + " is greater")