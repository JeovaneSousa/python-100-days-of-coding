from turtle import Turtle, Screen
from scoreboard import Scoreboard
from ball import Ball
from controller import Controller
from controller import POSITION
import time
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

left_paddle = Controller(POSITION[0])
right_paddle = Controller(POSITION[1])
ball = Ball()
screen.listen()
scoreboard = Scoreboard()

screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

is_game_on = True

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.refresh()
        scoreboard.l_score()
        scoreboard.update_score()

    if ball.xcor() < - 380:
        ball.refresh()
        scoreboard.r_score()
        scoreboard.update_score()

    if scoreboard.left_score == 5 or scoreboard.right_score == 5:
        is_game_on = False
        scoreboard.game_over()

screen.exitonclick()
