row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}\n")

position = input("Where do you want to put the treasure? Type two numbers: The first will refer to the colum number and the second, the row number.\n ")
y = int(position[0])-1
x = int(position[1])-1

map[x][y] = "X"
print(f"{row1}\n{row2}\n{row3}\n")
