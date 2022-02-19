logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
import random
import os
import sys

def dealCards(number_of_cards_to_draw, hand):

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    for draw_times in range(0,number_of_cards_to_draw):
        random_card = random.choice(cards)
        hand.append(random_card)
    return hand

def calculatescore(player_score):
    return sum(player_score)

def checkScore(player_hand, computer_hand, player_score,computer_score):

    if player_score == computer_score:
        result = print("It`s a tie!")
    elif player_score == 21 and computer_score != 21:
        result = print("Blackjack! You WIN!")
    elif computer_score == 21 and player_score != 21:
        result = print("Computer WINS. BlackJack!")
    elif computer_score > 21 and player_score > 21:
        result = print("It`s a tie.")
    elif computer_score > 21:
        result = print("Computer went over! You WIN!")
    elif player_score > 21:
        result = print("You went over. You lose =/")
    elif player_score < computer_score:
        result = print("Computer WINS!")
    elif player_score > computer_score:
        result = print("You WIN!")
    print(f"Your cards:{player_hand}, current score = {player_score} ")
    print(f"Computer score is {computer_score}. and it`s hand {computer_hand}")
    return result

def aceFix(hand):
    
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)

def blackJack():
    os.system('clear')
    player_hand = []
    computer_hand = []
    player_hand = dealCards(2, player_hand)
    computer_hand = dealCards(2, computer_hand)
    computer_score = calculatescore(computer_hand)
    player_score = calculatescore(player_hand)

    print(logo)
    print("Welcome to Blackjack!")

    continue_drawing = True
    while(continue_drawing):
        print(f"Your cards:{player_hand}, current score = {player_score} ")
        print(f"Computer first card: {computer_hand[0]}")
        
        if input("Type 'y' to get another card, type 'n' o pass: ") == "y":
            player_hand = dealCards(1, player_hand)
            aceFix(player_hand)
            player_score = calculatescore(player_hand)
        else:
            continue_drawing = False

        while(computer_score < 17):
            if computer_score < 17:
                computer_hand = dealCards(1, computer_hand)
                aceFix(computer_hand)
                computer_score = calculatescore(computer_hand)

    checkScore(player_hand=player_hand, computer_hand= computer_hand, player_score=player_score, computer_score=computer_score)
    play_again_question = input("Would like to continue playing? Type 'y' for yes and 'n' for no: ")
    if play_again_question == "y":
        os.system('clear')
        blackJack()
    else:
        sys.exit(0)

blackJack()
