amount_paid = float(input("How much did you pay? "))
cost = float(input("What was the cost of your purchase? "))

def change_calculator(amount_paid, cost):
    if amount_paid == cost:
        return 0
    elif amount_paid > cost:
        return amount_paid - cost
    else:
        return amount_paid - cost

print("The amount of change that is needed to be returned is", change_calculator(amount_paid, cost), "dollars")