import turtle
import random
turtle.shape("turtle")

lineNum = random.randint(3, 10)
lineLength = random.randint(50, 100)
angle = random.randint(0,360)

for i in range (lineNum):
    turtle.forward(lineLength)
    turtle.right(angle)

turtle.exitonclick()