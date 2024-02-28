def drawing_shape(sides):
    colors = ["red","green","blue","dark green","deep pink","cornflower blue","lawn green"]
    color = random.choice(colors)
    for i in range(sides):
        turtle.forward(100)
        turtle.right(360//sides)
    turtle.color(color)

from turtle import Turtle,Screen
import random
turtle  = Turtle()

sides = 3
for _ in range(3,11):
    drawing_shape(sides)
    sides+=1
screen = Screen()
screen.exitonclick()