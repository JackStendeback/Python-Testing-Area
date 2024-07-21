from coffee_shop_menu import MENU


# TODO: Need a function to get the water, milk, coffee, and price values from the data set.
def get_ingredients(drink):
    if drink in MENU:
        ingredients = MENU[drink]["ingredients"]
        water = ingredients.get("water", "no water found")
        milk = ingredients.get("milk", "0")
        coffee = ingredients.get("coffee", "no coffee found")
        price = MENU[drink]["cost"]
        print(f"A {drink} has {water}oz of water, {milk}oz of milk and {coffee}oz of coffee. Cost: ${price}")


# TODO: Welcome user to the coffee shop, and ask them what drink they would like to order.
print("Welcome to Jack's Coffee Shop!")
print("Here is a look at our menu.")
get_ingredients('espresso')
get_ingredients('latte')
get_ingredients('cappuccino')

user_selection = input("'Espresso'. 'Latte', or 'Cappuccino'?: ").lower()

# TODO: Make sure shop has sufficient ingredients to make the drink.
