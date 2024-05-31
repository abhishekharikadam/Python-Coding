# Program to make simple calculator

num1 = float(input("Enter a 1st number:- "))
num2 = float(input("Enter a 2st number:- "))

print ("\nPress 1 for addition \nPress 2 for subtraction \nPress 3 for multiplication \nPress 4 for division \n")

choice = int(input("Enter your choice from 1 to 4:- "))

if choice == 1:
    print("The addition of given numbers is ", num1 + num2)
elif choice == 2:
    print("The subtraction of given numbers is ",num1 - num2)
elif choice == 3:
    print("The multiplication of given numbers is ",num1 * num2)
elif choice == 4:
    print("The division of given numbers is ",num1 / num2)
else:
    print("Invalid input")