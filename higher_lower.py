import random
from higher_lower_gamedata import data
from higher_lower_art import logo, versus

print(logo)

points = 0
while_running = True


def get_new_option(exclude_name=None):
    option_entry = random.choice(data)
    while exclude_name and option_entry['name'] == exclude_name:
        option_entry = random.choice(data)
    return option_entry


# Initial options setup
option_1_entry = get_new_option()
name_1 = option_1_entry['name']
description_1 = option_1_entry['description']
country_1 = option_1_entry['country']
follower_1 = option_1_entry['follower_count']


def questions(name_1, description_1, country_1, name_2, description_2, country_2):
    print(f"Compare A: {name_1}, a {description_1}, from {country_1}.")
    print(versus)
    print(f"Against B: {name_2}, a {description_2}, from {country_2}.")


while while_running:
    option_2_entry = get_new_option(exclude_name=name_1)
    name_2 = option_2_entry['name']
    description_2 = option_2_entry['description']
    country_2 = option_2_entry['country']
    follower_2 = option_2_entry['follower_count']

    questions(name_1, description_1, country_1, name_2, description_2, country_2)

    user_selection = input("Who has more followers? Type 'A' or 'B': ")

    if user_selection == 'A' and follower_1 > follower_2:
        print(f"Correct! {name_1} has more followers than {name_2}")
        points += 1
        # Option 1 remains the same, get a new option 2 for the next round
    elif user_selection == 'B' and follower_2 > follower_1:
        print(f"Correct! {name_2} has more followers than {name_1}")
        points += 1
        # Option 2 becomes the new option 1
        name_1, description_1, country_1, follower_1 = name_2, description_2, country_2, follower_2
    else:
        print("Sorry, you were incorrect.")
        print(f"Your final score was {points} points.")
        while_running = False
