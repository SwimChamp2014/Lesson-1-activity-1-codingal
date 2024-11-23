unit = int(input("How many units have you consumed: "))

if unit < 50:
    amount = unit * 2.60
    tax = 25

elif unit > 50 and unit <= 100:
    amount = unit * 3.25
    tax = 35

elif unit > 100 and unit <+ 200:
    amount = unit * 5.26
    tax= 45

else:
    amount = 8.45 * unit
    tax = 75

print(f" Your electricity bill is {amount + tax}")