import random
import sys
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator ! ")

try:
    n_letters = int(input("How many letters would you like in your password? \n"))
except ValueError:
    print("Error: You should stick to numbers")
    sys.exit(1)
try:
    n_symbols = int(input("How many symbols would you like ? \n"))
except ValueError:
    print("Error: You should stick to numbers")
    sys.exit(1)
try:
    n_numbers = int(input("How many numbers would you like ? \n"))
except ValueError:
    print("Error: You should stick to numbers.")
    sys.exit(1)

password_list = []

for i in range(0, n_letters):
    password_list.append(random.choice(letters))

for i in range(0, n_symbols):
    password_list.append(random.choice(symbols))

for i in range(0, n_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""
for i in password_list:
    password += str(i)
    
print(f"Here is your password: {password}")
