import turtle
pen=turtle.Pen()
pen.speed(0)
pen.color("red","yellow")
pen.begin_fill()
for var in range(220):
    pen.forward(180)
    pen.left(160)
pen.end_fill()
turtle.exitonclick()