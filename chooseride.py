print("Select your ride: ")
print("1. Bike")
print("2. Car")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("What type of bike? ")
    print("1. Scooty\n")
    print("2. Scooter\n")

    choice2 = int(input("Enter your second choice: "))
    if choice2 == 1:
        print("you have selected a scooty") 
    else:
        print("you have selected a scooter")

elif choice == 2:
    print("Choose between\n1. Sedan\n2. Lambo")
    choice3 = int(input("enter your choice: "))


    if choice3 == 1:
        print("You have chosen a sedan")
    else: 
        print("You have selected a Lambo")


