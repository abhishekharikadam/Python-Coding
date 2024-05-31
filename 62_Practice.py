# Program to check whether a string is Palindrome or not

a = input("Enter a word here:- ")

rev = a[::-1]

if a == rev:
    print("It is a Palindrome")
else:
    print("It is not palindrome")