import random
import os
import sys
logo = '''  ______                                                   __      __                        __    __                          __                           
 /      \                                                 |  \    |  \                      |  \  |  \                        |  \                          
|  $$$$$$\ __    __   ______    _______   _______        _| $$_   | $$____    ______        | $$\ | $$ __    __  ______ ____  | $$____    ______    ______  
| $$ __\$$|  \  |  \ /      \  /       \ /       \      |   $$ \  | $$    \  /      \       | $$$\| $$|  \  |  \|      \    \ | $$    \  /      \  /      \ 
| $$|    \| $$  | $$|  $$$$$$\|  $$$$$$$|  $$$$$$$       \$$$$$$  | $$$$$$$\|  $$$$$$\      | $$$$\ $$| $$  | $$| $$$$$$\$$$$\| $$$$$$$\|  $$$$$$\|  $$$$$$\
| $$ \$$$$| $$  | $$| $$    $$ \$$    \  \$$    \         | $$ __ | $$  | $$| $$    $$      | $$\$$ $$| $$  | $$| $$ | $$ | $$| $$  | $$| $$    $$| $$   \$$
| $$__| $$| $$__/ $$| $$$$$$$$ _\$$$$$$\ _\$$$$$$\        | $$|  \| $$  | $$| $$$$$$$$      | $$ \$$$$| $$__/ $$| $$ | $$ | $$| $$__/ $$| $$$$$$$$| $$      
 \$$    $$ \$$    $$ \$$     \|       $$|       $$         \$$  $$| $$  | $$ \$$     \      | $$  \$$$ \$$    $$| $$ | $$ | $$| $$    $$ \$$     \| $$      
  \$$$$$$   \$$$$$$   \$$$$$$$ \$$$$$$$  \$$$$$$$           \$$$$  \$$   \$$  \$$$$$$$       \$$   \$$  \$$$$$$  \$$  \$$  \$$ \$$$$$$$   \$$$$$$$ \$$      
                                                                                                                                                            
                                                                                                                                                            
                                                                                                                                                           '''

def set_game_level():
    game_level = input("Choose a difficulty. Type 'easy' or 'hard'. ").lower()
    if game_level == "easy":
        total_attempts = 10
    else:
        total_attempts = 5
    return total_attempts
       
def take_a_guess(total_attempts):
    print(f"You have {total_attempts} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))
    return guess

def check_score(random_number,total_attempts):
    while(total_attempts > 0):
        guess = take_a_guess(total_attempts)       
        if guess == random_number:
            print("Yes! You guessed right")
            print(f"The result was {random_number} !")
            continue_or_stop()
        elif guess > random_number:
            print("Too high.")
            total_attempts -= 1
        else:
            print("Too low. ")
            total_attempts -= 1
            
    print("You ran out of attempts. You lost! ")
    print(f"The result was {random_number} !")
    continue_or_stop()

def continue_or_stop():
    answer = input("Would you like to play gain ? Type 'y' for yes or 'n' for no. ").lower()
    if answer == "y":
        play_game()
    else:
        sys.exit(0)

def play_game():
    os.system('clear')
    print(logo)
    print("Welcome to the Number Guessing Game! ")
    print("I`m thinking of a number from 1 and 100")
    random_number = random.randint(1,100)
    total_attempts = set_game_level()
    check_score(random_number=random_number,total_attempts=total_attempts)
    

play_game()