from turtle import Turtle,Screen
import random

class Food(Turtle):


    def foods(self):
        #
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
        return self
    
    def refresh(self):
        x = random.randint(-230, 230)
        y = random.randint(-230, 230)
        self.goto(x, y)

