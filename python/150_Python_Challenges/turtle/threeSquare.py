import turtle
turtle.shape("turtle")

for i in range(3):
    for i in range(4):
        turtle.pendown()
        turtle.forward(50)
        turtle.right(90)
    turtle.penup() 
    turtle.forward(70)

turtle.exitonclick()