from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO: Print report
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True

money_machine.report()
coffee_maker.report()
# TODO: Check if resource sufficient
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine = MoneyMachine()
        coffee_maker = CoffeeMaker()
    else:
        drink = menu.find_drink(choice)
        # TODO: Check if transaction successful
        if coffee_maker.is_resource_sufficient(drink):
            # TODO: Process Coins
            if money_machine.make_payment(drink.cost):
                # TODO: Make Coffee
                coffee_maker.make_coffee(drink)
