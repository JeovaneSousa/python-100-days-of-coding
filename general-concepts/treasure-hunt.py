print('''
     .-""""""-.
   .'          '.
  /   O    -=-   \
 :                :
 |                |  winking
 : ',          ,' :
  \  '-......-'  /
   '.          .'
jgs  '-......-'
''')

print("Welcome to Treasure Hunt.")
print("Your mission is to find the missing trasure!")

answer = input("You wake up half way up in a very tall and freezing mountain you can only go two ways. Which direction you choose? 'up' or 'down'? \n").lower()

if answer == "up":
    answer = input("You reach a cave. It`s really dark inside. Do you go 'in' or continue 'climbing'? \n").lower()
    if answer == "in":
        answer = input("There are two paths inside the cave. One brighter the other is so dark no light can be seen. Which way do you go ? The 'Bright' or 'Dark' path? \n ").lower()
        if answer == "dark":
            answer = input("You walk for a while through the darkness. Eventually you see something sparkling. A bright yellow glow shines from a chest. The treasure is right there, ripe for the taking. What do you do? Run for the trasure? turn back and leave the treasure there or walk carefully towards the treasure. What do you do? 'run', 'walk' or 'turn back' \n").lower()
            if answer == "walk":
                print("You see a whole on the ground, jump over it, and get to the treasure. While you are there you see a giant bear getting closer. It sees the whole on the ground, turns back and leaves. Eventually you leave the cave a rich person. Yay! Enjoy! You WIN! \n ")
            elif answer == "turn back":
                print("You find yourself face to face with a mama Bear and her cubs. She charges at you. Game over.")
            else:
                print("You didn`t see a whole on the ground on the way to the treasure. You fall from a height of 200m. Game over.")
        else:
            print("You find yourself face to face with a mama Bear and her cubs. She charges at you. Game over.")
    else:
        print("There is a sudden Avalanche. It hits you and throws you from the edge. Game over.\n")
else:
    print("You step into uneasy snow and falls from the edge. Game over.\n")