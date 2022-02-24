# TODO 1 Generate 2 random indexes to acess the data list
# TODO 2 Acess the name, description and country of the random selected data
# TODO 3 Asks for a input from the user to select if it`s higher or lower based on followers count
# TODO 4 If the right answer is B, assign the B option to the A`s place.

import os
import random
import sys

from data import data
from art import logo,vs

game_score = 0
index_a = random.randint(0, len(data) - 1)
continue_game = True


def printoptions(game_score, index_a, index_b):
    name_a = data[index_a]["name"]
    description_a = data[index_a]["description"]
    country_a = data[index_a]["country"]

    name_b = data[index_b]["name"]
    description_b = data[index_b]["description"]
    country_b = data[index_b]["country"]

    print(logo)
    print(f"Your current score is {game_score}")
    print(f"Compare A: {name_a}, a {description_a} from {country_a}.")
    print(vs)
    print(f"Compare B: {name_b}, a {description_b} from {country_b}.\n")


def getfollowercount(index):
    follower_count = data[index]["follower_count"]
    return follower_count


while continue_game:
    index_b = random.randint(0, len(data) - 1)
    if index_b == index_a:
        index_b = random.randint(0, len(data) - 1)
    a_follower_count = getfollowercount(index=index_a)
    b_follower_count = getfollowercount(index=index_b)
    printoptions(game_score, index_a=index_a, index_b=index_b)
    player_choice = input("Who has a higher follower count on instagram: 'A' or 'B'?").upper()

    is_the_answer_b = False
    if a_follower_count > b_follower_count:
        right_answer = "A"
    else:
        right_answer = "B"

    if player_choice == right_answer:
        game_score += 1
        os.system('clear')
        if right_answer == "B":
            is_the_answer_b = True
        else:
            is_the_answer_b = False
    else:
        os.system('clear')
        print(f"You are wrong! You lost. Your score was: {game_score}.")
        continue_game = False
        sys.exit(1)
    if is_the_answer_b:
        index_a = index_b
