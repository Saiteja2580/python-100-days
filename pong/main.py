from turtle import Turtle,Screen
from game_screen import Screen1
from peddle import Peddle
from pong import Pong
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")




game_is_on = True



screen.tracer(0)
left_paddle = Peddle()
right_paddle = Peddle()
left_paddle.peddle(-350,0)
right_paddle.peddle(350,0)
pong = Pong()

while game_is_on:
    
    screen.update()
    screen.onkey(left_paddle.move_forward,"Up")
    screen.onkey(left_paddle.move_backward,"Down")
    screen.onkey(right_paddle.move_forward,"Left")
    screen.onkey(right_paddle.move_backward,"Right")
    screen.listen()
    time.sleep(0.2)
    pong.pong_right()

    if pong.distance(right_paddle) < 50 and pong.xcor() > 340:
        pong





screen.exitonclick()

