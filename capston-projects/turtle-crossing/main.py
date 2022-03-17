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

player = TurtlePlayer()
manage = CarManager()
score = ScoreBoard()
screen.tracer(0)
screen.onkey(player.move_up, "Up")
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)

    manage.create_cars()
    manage.move_cars()
    score.write_score()
    for cars in manage.list_of_cars:
        if player.distance(cars) < 25:
            score.write_game_over()
            is_game_on = False

    if player.ycor() > 280:
        manage.finish_line(score)
        player.reset_position()
        score.write_score()

screen.exitonclick()