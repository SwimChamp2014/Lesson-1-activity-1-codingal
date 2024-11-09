medicalstatus = input("Do you have any medical conditions (Y=Yes/N=No): ")
attendance = int(input("Please enter your attendance: "))

if medicalstatus == "Y":
    print("You are allowed to take the exam")

if medicalstatus == "N" and attendance <= 75:
    print("You are not allowed to take the test")

if medicalstatus == "N" and attendance > 75:
    print("You are allowed to take the test")


    