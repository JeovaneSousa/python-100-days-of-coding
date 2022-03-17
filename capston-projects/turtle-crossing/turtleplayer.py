from turtle import Turtle

MOVE_DISTANCE = 10


class TurtlePlayer(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.setheading(90)
        self.reset_position()

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.goto(x=0, y=-280)