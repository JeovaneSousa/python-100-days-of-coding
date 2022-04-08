from turtle import Turtle

FONT = ("Ariel", 24, "normal")
ALIGNMENT = "center"
highest_score = 0


class Board(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as score:
            self.highest_score = int(score.read())
        self.penup()
        self.goto(x=0, y=260)
        self.color('white')
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"SCORE: {self.score} HIGHEST SCORE: {self.highest_score}", move=False, align=ALIGNMENT, font=FONT)

    def score_refresh(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
        with open("data.txt", mode="w") as highest:
            highest.write(f"{self.highest_score}")
        self.score = 0
        self.update_score()
