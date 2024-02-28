from turtle import Turtle


class Screen1(Turtle):

    coord = -250

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.pencolor("white")
        self.goto(0,-250)
        self.setheading(90)


    def draw_screen(self):
        while self.coord < 250:
            self.pendown()
            self.pensize(5)
            self.forward(10)
            self.penup()
            self.forward(10)
            self.coord = self.coord+10
