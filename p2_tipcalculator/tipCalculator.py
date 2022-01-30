#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
ten_p = 10
twelve_p = 12
fifteen_p = 15

print("Welcome to the tip calculator.")

bill = float(input("What was the total bill?\n"))

percentage = float(input(f"What percentage tip would like to give, {ten_p}, {twelve_p} or {fifteen_p}?\n"))
percentage /= 100

npeople = int(input("How many people to split the bill?\n"))

result = round((bill + (bill * percentage)) / npeople,2)

print(f"Each person should pay: ${result}")