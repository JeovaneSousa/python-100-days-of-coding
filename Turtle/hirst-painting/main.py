import turtle

import colorgram
from turtle import Turtle, Screen
import random

# list_of_color = colorgram.extract("image.jpg", 30)
#
# rgb_colors = []
#
# for color in list_of_color:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#     print (rgb_colors)
turtle.colormode(255)
color_list = [(152, 72, 58), (41, 126, 82), (241, 223, 195), (197, 151, 119), (154, 59, 78), (13, 19, 41),
              (107, 172, 213), (115, 184, 151), (39, 14, 24), (43, 16, 10), (43, 107, 147), (199, 235, 215),
              (56, 171, 128), (234, 211, 101), (152, 27, 42), (208, 68, 81), (9, 40, 20), (242, 215, 226),
              (151, 29, 21), (195, 221, 238), (202, 83, 75), (198, 135, 156), (11, 101, 54), (134, 223, 185),
              (31, 36, 153), (46, 161, 187), (84, 111, 199), (248, 163, 152), (166, 151, 58), (134, 215, 231)]

painter = Turtle()
painter.speed("fastest")
painter.setheading(225)
painter.penup()
painter.forward(300)
painter.setheading(0)


def paint_line():
    for i in range(10):
        painter.dot(20, random.choice(color_list))
        painter.penup()
        painter.forward(50)
        painter.pendown()
    reset()


def reset():
    painter.penup()
    painter.setheading(90)
    painter.forward(50)
    painter.setheading(180)
    painter.forward(500)
    painter.setheading(0)


def hist_painting(number_of_rows):
    for i in range(number_of_rows):
        paint_line()


hist_painting(10)






screen = Screen()
screen.exitonclick()
