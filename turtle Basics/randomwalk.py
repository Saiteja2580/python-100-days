from turtle import Turtle,Screen
import turtle
import random

#colormode is used to set the range of rgb to 1 or 255 
turtle.colormode(255)

directions = [0,90,180,270]

def random_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

turtle = Turtle()
turtle.speed(0)
for i in range(0,200):
    turtle.pensize(10)
    turtle.forward(25)
    turtle.setheading(random.choice(directions))
    turtle.color(random_colour())
screen = Screen()
screen.exitonclick()