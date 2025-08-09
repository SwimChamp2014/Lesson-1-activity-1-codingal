import math

class Circle:
    def __init__(self, radius):
        # Ensure radius is a positive number
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    def area(self):
        # Calculate and return the area
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        # Calculate and return the perimeter (circumference)
        return 2 * math.pi * self.radius

# Separate user input from the class itself
try:
    user_radius = float(input("Enter the radius of the circle: "))
    circle = Circle(user_radius)

    print("The area of the circle is:", circle.area())
    print("The perimeter of the circle is:", circle.perimeter())
except ValueError as e:
    print("Invalid input:", e)