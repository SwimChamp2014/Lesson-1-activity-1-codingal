x = int(input("Enter a number: "))


try:
    if type(x) != int:
        raise ValueError
    else: 
        print(x)

except ValueError as error:
    print("Error: ", error)


y = int(input("Enter a number: "))

try:
    if y == 0:
        raise ZeroDivisionError
    else:
        print(x/y)

except ZeroDivisionError:
    print("Error: " , ZeroDivisionError)





    

