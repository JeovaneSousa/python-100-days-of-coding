from turtle import Screen, Turtle

from turtleplayer import TurtlePlayer
from carmanager import CarManager
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.title("Turtle Crossing")
screen.listen()

screen.tracer(0)
player = TurtlePlayer()
manage = CarManager()
score = ScoreBoard()
screen.onkey(player.move_up, "Up")
is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)

    manage.create_cars()
    manage.move_cars()

    # Detect collision with car.
    for cars in manage.list_of_cars:
        if player.distance(cars) < 25:
            player.reset_position()
            manage.reset_manager()
            score.update_highest_score()

    # Detect when you cross the finish line
    if player.ycor() > 280:
        manage.next_level()
        player.reset_position()
        score.next_level()

screen.exitonclick()
