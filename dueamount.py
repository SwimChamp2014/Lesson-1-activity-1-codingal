cost = int(input("Enter the cost of the product in dollars: "))
paid = int(input("Enter how much you payed: "))

if cost != paid and cost > paid:
    new_amount = cost - paid
    print("You need to pay {} more dollar(s)".format(new_amount))


if cost < paid and cost != paid:
    new_amount = paid-cost
    print("The change is {} dollar(s)".format(new_amount))


if cost == paid:
    print("You have paid the perfect amount! ")