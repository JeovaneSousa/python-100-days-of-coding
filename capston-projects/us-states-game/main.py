import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data["state"].tolist()
correct_guesses = []
score = 0
game_is_on = True

while game_is_on:
    answer_state = screen.textinput(f"Guess the state. {score}/50", "Try a guess").title()
    if answer_state == "Exit":
        break
    if answer_state in states_list:
        if answer_state not in correct_guesses:
            score += 1
            correct_guesses.append(answer_state)
            x_cord = int(data[data["state"] == answer_state]["x"])
            y_cord = int(data[data["state"] == answer_state]["y"])
            state_on_screen = turtle.Turtle()
            state_on_screen.penup()
            state_on_screen.hideturtle()
            state_on_screen.goto(x=x_cord, y=y_cord)
            state_on_screen.write(f"{answer_state}", True, "center", font=("arial", 8, "normal"))
        if score == 50:
            game_is_on = False

missing_states = [state for state in states_list if state not in correct_guesses]
missing_states_dict = {"Missing States": missing_states}
missing_states_dataframe = pandas.DataFrame(missing_states_dict)
missing_states_dataframe.to_csv("missing_states.csv")
