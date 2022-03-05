import random
from turtle import Turtle, Screen

is_race_on = True
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win ? Enter a color: ").lower()
y_list = [80, 40, 0, -40, -80, -120, ]
turtle_colors = ["red", "orange", "yellow", "green", "blue", "purple", ]

turtles = []
for i in range (0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(turtle_colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_list[i])
    new_turtle.speed(1)
    turtles.append(new_turtle)

while(is_race_on):
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            if turtle.pencolor() == user_bet:
                print(f"You've won! The winning turtle was: {turtle.pencolor()}!")
            else:
                print(f"You've Lost! The winning turtle was {turtle.pencolor()}!")
        random_movement = random.randint(0, 10)
        turtle.forward(random_movement)


screen.exitonclick()
