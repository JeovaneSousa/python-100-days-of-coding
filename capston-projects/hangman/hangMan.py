
import random
import sys
import os


logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel","dragon","husky","lion","tiger","monkey","fish","shark","dinossaur","whale","dolphin","octopus"]
misses = ""
lives_counter = 6
blank_word = []
chosen_word = random.choice(word_list)

print(logo)
print("Welcome !\n\n")

for index in range(0,len(chosen_word)):
    blank_word += "_"  

while lives_counter > 0:

    guess = input("Guess a letter: ").lower()
    
    os.system('clear')

    bool = False
    for index in range(0,len(chosen_word)):
        if chosen_word[index] == guess:
            blank_word[index] = guess
            bool = True

    if not bool:
        lives_counter -= 1
        misses += guess

#Game aesthethics
    print("--------------------------------------------------------------------------")
    print("\n")
    print(*blank_word)
    print("\n")
    print(stages[lives_counter])
    print("\n")
    print(f"Misses: {misses}")
    print("\n")
    print("--------------------------------------------------------------------------")
       
    if "".join(blank_word) == chosen_word:
        print("YOU WIN ! ")
        sys.exit(0)

print(f"The word was: {chosen_word} \n")
print("YOU LOSE !")
    




