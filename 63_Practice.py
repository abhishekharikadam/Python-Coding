# Program to remove Panctuations from a string

punc = """!@#$%^&*()_+=[{:;'",<.>/?}]/*-+"""

string = input("Enter anything here:- ")

empty_string = ""

for i in string:
    if i not in punc:
        empty_string += i

print(empty_string)