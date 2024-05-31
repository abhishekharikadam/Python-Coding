marks = int(input("Enter the marks:- "))

if(marks>=90):
    print("You have passed the exams with extraordinary score")
elif(marks>=75 and marks<=89):
    print("You have passed the exams with Excellent score")
elif(marks>=65 and marks<=74):
    print("You have passed the exams with Better score")
elif(marks>=45 and marks<=64):
    print("You have passed the exams with Good score")
elif(marks>=35 and marks<=44):
    print("You have passed the exams with Poor score")
else:
    print("You have failed in exams")