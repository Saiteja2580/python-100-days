from turtle import Turtle,Screen

ben = Turtle()
for i in range(15):
    ben.forward(10)
    ben.penup()
    ben.forward(10)
    ben.pendown()


screen = Screen()
screen.exitonclick()