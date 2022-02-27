from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffemachine = CoffeeMaker()
coffe_menu = Menu()
money_machine = MoneyMachine()


is_on = True
options = coffe_menu.get_items()
while (is_on):
    users_choice = input(f"What would like to order? These are the options:  {options} \n").lower()
    if users_choice == "off":
        is_on = False
    elif users_choice == "report":
        coffemachine.report()
    else:
        drink = coffe_menu.find_drink(users_choice)
        print(f"The cost of a {drink.name} is: ${drink.cost}")
        if coffemachine.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffemachine.make_coffee(drink)