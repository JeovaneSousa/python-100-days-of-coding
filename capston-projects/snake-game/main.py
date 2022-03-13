from turtle import Screen
from snake import Snake
from food import Food
from score_board import Board
import time

screen = Screen()
screen.setup(startx=600, starty=600)
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
        is_game_on = False
        board.game_over()

    for segment in snake.segments[3:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            board.game_over()

    screen.onkey(snake.move_up, 'Up')
    screen.onkey(snake.move_down, 'Down')
    screen.onkey(snake.turn_left, 'Left')
    screen.onkey(snake.turn_right, 'Right')









screen.exitonclick()