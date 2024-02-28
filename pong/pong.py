from turtle import Turtle

class Pong(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("circle")

    def pong_right(self):
        x_coord = self.xcor()+10
        y_coord = self.ycor()+10
        self.goto(x_coord,y_coord)
        if self.xcor() >= 280:
            x_coord = self.xcor()+10
            y_coord = self.ycor()-30
            self.goto(x_coord,y_coord)

            

        