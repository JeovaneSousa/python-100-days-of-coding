import random
import sys

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''


paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''


scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#Write your code below this line 👇
try:
    user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
except ValueError:
    print("Error: You should stick to the numbers 0,1 or 2.") 
    sys.exit(1)
    
opponent = random.randint(0,2)
rockpaperscissors = [rock,paper,scissors]

try:
    print("You play:")
    a = print(rockpaperscissors[user_input])
except (IndexError, ValueError, NameError) as e:
    print("Error: You should stick to the numbers 0,1 or 2.") 
    sys.exit(1)

print("opponent plays:")
b = print(rockpaperscissors[opponent])

if user_input == opponent:
    print("It`s a draw!")
elif user_input == 0 and opponent == 1:
    print("You lost!")
elif user_input == 0 and opponent == 2:
    print("You win!")
elif user_input == 1 and opponent == 0:
    print("You win!")
elif user_input == 1 and opponent == 2:
    print("You lost!")
elif user_input == 2 and opponent == 0:
    print("You lost!")
elif user_input == 2 and opponent == 1:
    print("You win!")
