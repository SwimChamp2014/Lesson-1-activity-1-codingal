import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(400, 400)
pen = turtle.Turtle()


shape = input("Which shape do you want to draw [hexagon, square, pentagon]: ")

if shape == "pentagon" or "Pentagon":#don't do this next time, since it confuses the computer(specifically using or), look at the sample of this to understand what to do
    side_length = int(input("What is the side length that you want: "))
    num_sides1 = 5
    angle = 360/num_sides1
    pen.begin_fill()

    for i in range (num_sides1):
        pen.forward(side_length)
        pen.right(angle)

    pen.end_fill()

elif shape == "hexagon" or "Hexagon":
    num_sides = 6
    side_length = int(input("Enter the side length you want: "))
    angle = 360/num_sides
    pen.begin_fill()

    for i in range(num_sides):
        pen.forward(side_length)
        pen.right(angle)

    pen.end_fill()
# How come when I run this and type in hexagon it still draws a pentagon

turtle.done()