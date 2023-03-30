from turtle import Turtle, Screen
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('white')
        self.random_position()

    def refresh(self):
        self.random_position()

    def random_position(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(x=random_x, y=random_y)