# Program to sort Words in Alphabetical Order

# a = "Harry potter and the Goblet of Fire"
a = input("Enter something here:- ")

w = a.split()
for i in range (len(w)):
    w[i] = w[i].lower()

# print(w)
w.sort()
# print(w)

for i in w:
    print(i)