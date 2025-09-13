numbers = int(input("Enter a number: "))

even = numbers % 2 == 0
odd = not even

if even:
    print("The number you inputed is even. ")
else:
    print("The number you inputed is odd. ")