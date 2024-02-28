
from turtle import Turtle,Screen
from food import Food
import time
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    coord = 0
    coords = [(0,0),(-20,0),(-40,0)]

    screen = Screen()

    def __init__(self):
        self.segment_list = []
        self.snakeBody()
        self.head = self.segment_list[0]
    def snakeBody(self):
        for i in self.coords:
            self.add_newcomponent(i)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def movement(self):
            for i in range(len(self.segment_list)-1,0,-1):
                xcor = self.segment_list[i-1].xcor()
                ycor = self.segment_list[i-1].ycor()
                self.segment_list[i].goto(xcor,ycor)


            # if self.head.ycor() in COLLISION_POINTS:
            #     exit()


            self.head.forward(20)

    def add_newcomponent(self,position):
        turtle = Turtle()
        turtle.penup()
        turtle.shape("square")
        turtle.color("white")
        turtle.goto(position)
        self.segment_list.append(turtle)

    def extend(self):
        self.add_newcomponent(self.segment_list[-1].position())



