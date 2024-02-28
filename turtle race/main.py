from turtle import Turtle,Screen
import random


def turtle_creation(name, x1, y1, colour):
    name = Turtle()
    name.shape("turtle")
    name.color(colour)
    name.penup()
    name.goto(x=x1, y=y1)
    name.speed(10)
    return name

# tim = Turtle()
# tim.goto(x=-250,y=100)
# ben = Turtle()
# ben.goto(x=-250,y=50)
# jim = Turtle()
# jim.goto(x=-250,y=0)
# carol = Turtle()
# carol.goto(x=-250,y=-50)
# cap = Turtle()
# cap.goto(x=-250,y=-100)
# bob = Turtle()
# bob.goto(x=-250,y=-150)


is_game_on = False

screen = Screen()
screen.setup(width=500,height=500)
user_colour = screen.textinput(title="Turtle race",prompt="Enter a turtle color you bet on ?")

tim = turtle_creation("tim", -200, 150, "red")
ben = turtle_creation("ben", -200, 100, "green")
jim = turtle_creation("jim", -200, 50, "blue")
carol = turtle_creation("carol", -200, 0, "orange")
cap = turtle_creation("cap", -200, -50, "black")
bob = turtle_creation("bob", -200, -100, "violet")

racer_list = [tim,ben,jim,carol,cap,bob]


if user_colour:
    is_game_on = True

while is_game_on:
    
    for turtle in racer_list:
        randint = random.randint(0,10)
        turtle.forward(randint)
        if turtle.xcor() >= 230:
            is_game_on = False
            if turtle.color() == user_colour:
                print(f"You won the bet! {turtle.color()[0]} colour wins")
            else:
                print(f"You lose the bet! winner is {turtle.color()[0]}")
            break
        else:
            continue


screen.exitonclick()