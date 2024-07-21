# What can be ordered by the user, and what each drink consists of.
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
# Coffee Shop resources before ordering any product.
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# Currency value for the user.
money = 0

# Variable used to control the on/off power of the while loop controlling our coffee shop, and to have an off switch.
is_on = True
# While loop that prompts the user for a drink choice, shows funds/resources, and ends the transaction when needed.
while is_on:
    user_prompt = input("What would you like? (espresso/latte/cappuccino): ")
    if user_prompt == "stop":
        is_on = False
    elif user_prompt == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: ${money}")

# TODO: Step 4 of the Coffee Shop checklist is next, lets complete it!
