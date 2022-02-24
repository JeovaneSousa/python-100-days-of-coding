import random

names = input("Type all the names separated by a space and a coma.\n")
name_list = names.split(", ")
luck = random.randint(0,len(name_list)-1)

print(f"{name_list[luck]} is going to buy the meal today")