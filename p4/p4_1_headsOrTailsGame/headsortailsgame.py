import random

print("Head or Tails ? The computer will decide!\n")
side_choice = input("What side do you want to choose ? Heads or Tails? \n").lower()

#tails == 0
#heads == 1

print("\n-----------------------------------")
coin_toss = random.randint(0,1)

if coin_toss == 0:
    coin_toss = "tails"
else:
    coin_toss = "heads"

print("Here comes the coin toss... \n\n")
print(f"{coin_toss} \n")

if side_choice == coin_toss:
    print(f"{coin_toss} ! You win! ")
else:
    print(f"It`s {coin_toss}. You lost ! ")