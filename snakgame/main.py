import tkinter.messagebox
from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

XCOORD = [-300,300]


screen = Screen()
screen.bgcolor("black")
screen.setup(width=500,height=500)
screen.tracer(0)



snake = Snake()
food = Food()
food = food.foods()
gamescore = 0
score = Score()



screen.onkey(fun=snake.up,key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")
screen.listen()

is_game_on = True
while is_game_on:
    screen.update()
    snake.movement()
    time.sleep(0.2)
    if snake.head.xcor() >= 250 or snake.head.xcor() <= -250:
        is_game_on = False
        score.game_over()
    if snake.head.ycor() >= 250 or snake.head.ycor() <= -250:
        is_game_on = False
        score.game_over()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    for tail in snake.segment_list[1:]:
        if snake.head.distance(tail) < 10:
            is_game_on = False
            score.game_over()

        










screen.exitonclick()
