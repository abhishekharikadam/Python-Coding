sub1 = int(input("Enter subject 1 marks: "))
sub2 = int(input("Enter subject 2 marks: "))
sub3 = int(input("Enter subject 3 marks: "))

if(sub1<35):
    print("You have failed in subject 1")
elif(sub2<35):
    print("You have failed in subject 2")
elif(sub3<35):
    print("You have failed in subject 3")
elif(sub1 + sub2 + sub3)/3 < 40:
    print("You have failed in exam because total number of marks is not greater than 40")
else:
    print("Yoy have passed in exams!!!")