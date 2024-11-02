print("ENter Marks OBtained in 5 Subjects: ")
markone= int(input())
marktwo= int(input())
markthree= int(input())
markfour= int(input())
markfive= int(input())

total = markone+ marktwo + markthree + markfour + markfive
average = total/5

if average>= 91 and average <= 100:
    print("Your grade is A1")
if average>= 81 and average <= 91:
    print("Your grade is A2")
if average>= 71 and average <= 81:
    print("Your grade is B1")
if average>= 61 and average <= 71:
    print("Your grade is B2")
if average>= 51 and average <= 61:
    print("Your grade is C1")
if average>= 41 and average <= 51:
    print("Your grade is C2")
if average>= 33 and average <= 41:
    print("Your grade is D")
if average>= 21 and average <= 33:
    print("Your grade is E1")
if average>= 0 and average <= 21:
    print("Your grade is E2")
else:
    print("Invalid Input!")