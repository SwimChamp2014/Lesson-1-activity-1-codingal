try:
    age = int(input("Enter a number: "))
except ValueError:
    print("The number must be an integer. ")
    
if age % 2 == 0:
    print("the number you inputed is even. ")
else:
    print("Your number is odd. ")



