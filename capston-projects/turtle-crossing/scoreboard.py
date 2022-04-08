from turtle import Turtle

FONT = ("arial", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-280, 260)
        self.score = 0
        with open("data.txt",mode="r") as highest:
            self.highest_score = int(highest.read())
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.score} Highest Score: {self.highest_score}", font=FONT)

    def next_level(self):
        self.score += 1
        self.update_score()


    def update_highest_score(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("data.txt", mode="w") as highest:
                highest.write(f"{self.highest_score}")
        self.score = 0
        self.update_score()
