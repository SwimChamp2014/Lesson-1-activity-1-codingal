try:
    num1, num2 = eval(input("Please enter 2 numbers seperated by a comma: "))
    print("Result is, ", num1/num2)

except ZeroDivisionError:
    print("Division by zero results in an error! ")

except SyntaxError:
    print("Comma is missing, write in 2 numbers seperated by a comma like this: 1, 2")

except:
    print("Wrong input")

else:
    print("No exceptions")

finally:
    print("This will execute no matter what")