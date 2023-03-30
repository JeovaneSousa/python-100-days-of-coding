from turtle import Screen
from snake import Snake
from food import Food
from score_board import Board
import time

screen = Screen()
screen.setup(width=580, height=590, startx=0, starty=0, )
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
screen.listen()

board = Board()
snake = Snake()
food = Food()

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        board.score_refresh()
        snake.extend_snake()

    if snake.head.xcor() > 280 or snake.head.xcor() < - 280 or snake.head.ycor() > 280 or snake.head.ycor() < - 280:
        board.reset()
        snake.reset_snake()

    for segment in snake.segments[3:]:
        if snake.head.distance(segment) < 10:
            board.reset()
            snake.reset_snake()

    screen.onkey(snake.move_up, 'Up')
    screen.onkey(snake.move_down, 'Down')
    screen.onkey(snake.turn_left, 'Left')
    screen.onkey(snake.turn_right, 'Right')

screen.exitonclick()
