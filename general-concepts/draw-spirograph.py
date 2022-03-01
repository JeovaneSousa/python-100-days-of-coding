import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


directions = [0, 90, 180, 270]
ada = Turtle()
ada.speed("fastest")


def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        ada.circle(100)
        ada.setheading(ada.heading() + size_of_gap)
        ada.circle(100)
        ada.color(random_color())

draw_spirograph(5)

screen = Screen()
screen.exitonclick()
