from turtle import Turtle,Screen
import random

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,230)
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(f"Score : {self.score}",False,align="center",font=("Arial",13,"normal"))
    
    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score : {self.score}",False,align="center",font=("Arial",13,"normal"))

    def game_over(self):
        self.goto(x=0,y=0)
        self.write(f"GAME OVER",False,align="center",font=("Arial",18,"normal"))



