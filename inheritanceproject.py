class Vehicle:
    def __init__(self):
        distance = int(input("Enter the distance in miles: "))
        cost = distance * 5
        print("The cost for your ride in dollars is :", cost)




class Bus(Vehicle):
    pass


bus = Bus()

