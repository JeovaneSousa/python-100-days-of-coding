import random
import time
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

MOVE_INCREMENT = 10
CAR_POSITIONS = [(280, -200), (280, -120), (280, -80), (280, 0), (280, 80), (280, 120), (280, 200)]


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.starting_move_distance = 5
        self.list_of_cars = []

    def create_cars(self):
        car_production_frequency = random.randint(1, 6)
        if car_production_frequency == 1:
            new_car = Turtle('square')
            new_car.hideturtle()
            new_car.shapesize(1, 2, 1)
            new_car.penup()
            new_car.goto(random.choice(CAR_POSITIONS))
            new_car.showturtle()
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            self.list_of_cars.append(new_car)

    def move_cars(self):
        for car in self.list_of_cars:
            car.forward(self.starting_move_distance)

    def finish_line(self, scoreboard):
        scoreboard.score += 1
        self.starting_move_distance += MOVE_INCREMENT
