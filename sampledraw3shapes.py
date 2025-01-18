import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(400, 400)
pen = turtle.Turtle()

shape = int(input("Enter the Shape you want [ Hexagon, Pentagon, and Square] to draw as 1, 2, or 3 "))
if shape == 2:
    side_length = int(input("What is the side length that you want: "))
    num_sides = 5
    angle = 360/num_sides
    pen.begin_fill()

    for i in range (num_sides):
        pen.forward(side_length)
        pen.right(angle)

    pen.end_fill()

elif shape == 1:
    num_sides = 6
    side_length = int(input("Enter the side length you want: "))
    angle = 360/num_sides
    pen.begin_fill()

    for i in range(num_sides):
        pen.forward(side_length)
        pen.right(angle)

    pen.end_fill()

elif shape == 3:
    num_sides = 4
    side_length = int(input("Enter the side length you want: "))
    angle = 360/num_sides
    pen.begin_fill()

    for i in range(num_sides):
        pen.forward(side_length)
        pen.right(angle)

    pen.end_fill()

pen.hideturtle()

turtle.done()

# How come when I run this and type in hexagon it still draws a pentagon
#the reason it works is since in the b