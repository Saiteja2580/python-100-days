from turtle import Turtle,Screen
import turtle,random


turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)


def spirograph(size):
    for i in range(360//size):
        turtle.circle(100)
        turtle.penup()
        turtle.right(size)
        turtle.color(random_color())
        turtle.pendown()
        turtle.circle(100)



turtle = Turtle()
turtle.color("green")
turtle.speed(0)

spirograph(20)


screen = Screen()
screen.exitonclick()