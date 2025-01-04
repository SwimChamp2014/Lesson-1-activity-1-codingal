import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(400, 400)
pen = turtle.Turtle()
pen.color("red")
pen.fillcolor("green")

num_sides = int(input("How much sides do you want: "))
side_length = int(input("Enter the side length you want: "))
angle = 360/num_sides
pen.begin_fill()

for i in range(num_sides):
    pen.forward(side_length)
    pen.right(angle)

pen.end_fill()
pen.hideturtle()
#used to erase stuff  = pen.dot(400, "red")

turtle.done()