from turtle import Turtle

FONT = ("arial", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()

    def write_score(self):
        self.clear()
        self.penup()
        self.goto(-280, 260)
        self.write(f"Level: {self.score}", font=FONT)

    def write_game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=FONT)
