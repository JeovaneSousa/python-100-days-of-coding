
print("Welcome to Python Pizza Deliveries!")

bill = 0

size = input("What size pizza do you want? S, M, or L ")
size = size.lower()
if size == "s":
    bill += 15
elif size == "m":
    bill += 20
elif size == "l":
    bill += 25
else:
    print("Not a valid pizza size.")

add_pepperoni = input("Do you want pepperoni? Y or N ")
add_pepperoni = add_pepperoni.lower()

if add_pepperoni == "y" and size == "s":
    bill +=2
elif add_pepperoni == "y" and (size == "m" or size == "l"):
    bill +=3
else:
    print("Ok, No pepperoni then.")

extra_cheese = input("Do you want extra cheese? Y or N ")
extra_cheese = extra_cheese.lower()

if extra_cheese == "y":
    bill += 1
else:
    print("Ok, No extra cheese then.")

rounded_bill = round(bill,2)

print(f"Your final bill is: ${rounded_bill}.")