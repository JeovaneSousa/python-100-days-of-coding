from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.right_score = 0
        self.left_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 180)
        self.write(self.left_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 180)
        self.write(self.right_score, align="center", font=("Courier", 80, "normal"))

    def l_score(self):
        self.left_score += 1

    def r_score(self):
        self.right_score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 80, "normal"))
