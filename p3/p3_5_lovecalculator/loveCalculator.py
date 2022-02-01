print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#T  L
#R  O
#U  V
#E  E

combined_names = (name1 + name2).lower() 

t = combined_names.count("t")
print(f"T occurs {t} times.")
r = combined_names.count("r")
print(f"R occurs {r} times.")
u = combined_names.count("u")
print(f"U occurs {u} times.")
e = combined_names.count("e")
print(f"E occurs {e} times.\n")

l = combined_names.count("l")
print(f"L occurs {l} times.")
o = combined_names.count("o")
print(f"O occurs {o} times.")
v = combined_names.count("v")
print(f"V occurs {v} times.")
e = combined_names.count("e")
print(f"E occurs {e} times.")

true = str(t + r + u + e)
love = str(l + o + v + e)
love_score = int(true + love)

if love_score < 10 or love_score > 90:
    print(f"You score is {love_score}%, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}%, you are alright together.")
else:
    print(f"Your score is {love_score}%.")

