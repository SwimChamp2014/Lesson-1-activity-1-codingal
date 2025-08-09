class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12)
print('Vehicle name is:', School_bus.name, "The max speed is", School_bus.max_speed, "It's Mileage is:", School_bus.mileage)