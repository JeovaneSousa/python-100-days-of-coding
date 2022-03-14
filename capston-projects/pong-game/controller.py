from turtle import Turtle

POSITION = [(-350, 0), (350, 0)]


class Controller(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.penup()
        self.goto(position)
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)

    def move_up(self):
        self.goto(x=self.xcor(), y=self.ycor() + 20)

    def move_down(self):
        self.goto(x=self.xcor(), y=self.ycor() - 20)
