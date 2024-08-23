import turtle
import random
turtle.shape("turtle")

for i in range(8):
    turtle.color(random.choice(["red","pink", "green", "blue", "yellow", "orange"]))
    turtle.forward(50)
    turtle.right(45)

turtle.exitonclick()


# while True:
#     turtle.color(random.choice(["red","pink", "green", "blue", "yellow", "orange"]))
#     turtle.right(20)

# turtle.exitonclick()    