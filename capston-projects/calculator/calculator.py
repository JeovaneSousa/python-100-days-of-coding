import os

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multyply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

Calculator = {
    "+" : add,
    "-" : subtract,
    "*" : multyply,
    "/" : divide,
}
def calculator():
    print(logo)
    continue_operating = True
    first_number = float(input("What`s the first number?: "))
    while(continue_operating):
        for key in Calculator:
            print(key)
        operation_symbol = input("Pick an operation symbol from the lines above:")

        next_number = float(input("What`s the next number?: "))

        function = Calculator[operation_symbol]

        result = function(first_number, next_number)

        print(f"{first_number} {operation_symbol} {next_number} = {result}")

        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to exit and start a new calculation").lower() == "n":
            continue_operating = False
            calculator()
        else:
            first_number = result
            os.system('clear')

calculator()
