from turtle import Turtle, Screen

screen = Screen()
tim = Turtle()


def move_fowards():
    tim.forward(10)


def move_backwards():
    tim.back(10)


def move_right():
    tim.right(10)


def move_left():
    tim.left(10)


screen.listen()
screen.onkey(move_fowards, 'w')
screen.onkey(move_backwards, 's')
screen.onkey(move_right, 'd')
screen.onkey(move_left, 'a')
screen.onkey(screen.reset, 'c')

screen.exitonclick()
