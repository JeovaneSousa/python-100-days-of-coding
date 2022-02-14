import os 

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("Welcome to the Secret Auction Program")
bider_dict = {}
def add_bidder(name, bid):
    bider_dict[name] = bid

def check_bids():
    highest_value = 0
    winner = ""
    for key in bider_dict:
        if bider_dict[key] > highest_value:
            highest_value = bider_dict[key]
            winner = key
    print(f"The Winner is {winner} with a bid of ${highest_value}")

contiue_loop = True
while(contiue_loop):
    name = input("What is your name ? \n")
    bid = int(input("What`s your bid? $"))
    add_bidder(name = name, bid = bid)
    other_bider = input("Are there any other bidders? type 'yes' or 'no'. \n").lower()
    os.system('clear')
    if other_bider == "no":
        contiue_loop = False    
        print("And the winner is..")
        check_bids()





    

