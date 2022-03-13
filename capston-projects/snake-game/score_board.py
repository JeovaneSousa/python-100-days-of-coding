from turtle import Turtle
FONT = ("Ariel", 24, "normal")
ALIGNMENT = "center"


class Board(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(x=0, y=270)
        self.color('white')
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"SCORE: {self.score}", move=False, align= ALIGNMENT, font= FONT)

    def score_refresh(self):
        self.clear()
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)