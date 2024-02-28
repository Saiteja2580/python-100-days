import colorgram,turtle,random
from turtle import Turtle,Screen
# colors = colorgram.extract('spot painting\painting.webp',30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color = (r,g,b)
#     rgb_colors.append(color)

color_list = [(212, 154, 97), (52, 107, 131), (180, 78, 31), (199, 143, 34), (123, 80, 97), (117, 154, 170), (122, 176, 158), (229, 197, 127), (193, 86, 106), (55, 38, 20), (11, 51, 65), (194, 122, 142), (43, 169, 125), (53, 121, 116), (167, 22, 30), (226, 93, 79), (5, 29, 27), (244, 163, 160), (38, 32, 34), (80, 148, 169), (164, 26, 21), (239, 164, 168), (171, 208, 186), (105, 125, 159), (24, 81, 90), (26, 86, 81)]
timmy = Turtle()

timmy.hideturtle()
# going to corner of the page
timmy.setheading(220)
timmy.penup()
timmy.forward(300)
timmy.setheading(0)
timmy.pendown()
timmy.speed(0)
turtle.colormode(255)


#printing the dots in 10x10
for i in range(10):
    for j in range(10):
        timmy.dot(20,random.choice(color_list))
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()
    #moving turtke to the next line
    timmy.setheading(90)
    timmy.penup()
    timmy.forward(50)
    timmy.setheading(180)
    timmy.forward(500)
    timmy.setheading(0)
    timmy.pendown()
    


screen = Screen()
screen.exitonclick()