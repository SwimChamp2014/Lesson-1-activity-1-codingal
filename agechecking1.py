try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Please run it again and enter an integer")

if num >= 18:
    print("You have passed this requirement")
else:
    print("Your number isn't smaller than 18 ")

if num % 2 == 0:
    print("You have passed this requirement")

else:
    print("Your number is an odd number")
