number = int(input("Enter any number for the numerator: "))
number2 = int(input("Enter any number for the denominator: "))

if number%number2==0:
    print("numerator " + str(number) + " is divisible by " + str(number2))
else:
    print("numerator " + str(number) + " is not divisible by " + str(number2))