import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Creating a user and a computer variable
user = []
computer = []
game_running = True


def card_deal():
    return random.choice(cards)


def initial_deal():
    global user, computer
    user = [card_deal(), card_deal()]
    computer = [card_deal(), card_deal()]


def is_blackjack(hand):
    return sum(hand) == 21 and len(hand) == 2


def calculate_score(hand):
    score = sum(hand)
    if score > 21 and 11 in hand:
        score -= 10
    return score


while game_running:
    initial_deal()

    user_score = calculate_score(user)
    computer_score = calculate_score(computer)

    print(f"Users initial hand: {user} with a score of {user_score}")
    print(f"Computers initial hand: [{computer[0], "?"}] with a score of '?'")

    user_blackjack = is_blackjack(user)
    computer_blackjack = is_blackjack(computer)

    if user_blackjack:
        print("User has BlackJack!")
    else:
        pass

    if computer_blackjack:
        print("Computer has BlackJack")
    else:
        pass

    if computer_blackjack:
        print("Computer wins...")

    elif user_blackjack:
        print("You win!")

    go_again = input("Would you like to play another hand? yes or no?: ")
    if go_again == 'yes':
        initial_deal()
    else:
        game_running = False
