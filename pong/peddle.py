from turtle import Turtle


class Peddle(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=1,stretch_wid=5)

    def peddle(self,x_coord,y_coord):
        self.goto(x_coord,y_coord)

    def move_forward(self):
        new_y = self.ycor()+20
        self.goto(self.xcor(),new_y)

    def move_backward(self):
        new_y = self.ycor()-20
        self.goto(self.xcor(),new_y)
