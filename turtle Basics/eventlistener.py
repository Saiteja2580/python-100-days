from turtle import Turtle,Screen


tim = Turtle()

def forward():
    tim.forward(10)

def backward():
    tim.backward(10)


def up():
    tim.left(10)
    

def down():
    tim.right(10)



def clear():
    tim.clear()
    tim.penup()
    tim.home()





screen = Screen()
screen.onkey(forward,"Up")
screen.onkey(backward,"Down")
screen.onkey(up,"Left")
screen.onkey(down,"Right")
screen.onkey(clear,"c")

screen.listen()
screen.exitonclick()