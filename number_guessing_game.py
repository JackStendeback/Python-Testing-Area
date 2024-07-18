# TODO: Import the random module to get the random number for the game, define random variable.
import random
import number_guessing_art
print(number_guessing_art.logo)
random_number = random.randint(1, 100)
random_number = str(random_number)
# Printing random number for testing purposes.
# print(random_number)
game_running = True
# TODO: Welcome user to the number guessing game
print("Welcome to the Number Guessing Game!")
# TODO: Tell the user the parameters of the guess (1 to 100)
print("I'm thinking of a number between 1 and 100.")
# TODO: Ask user to choose a difficulty, either easy or hard.
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
# TODO: Show the user how many guesses they have remaining(10 for easy, 5 for hard)
attempts = 0
if difficulty == 'easy':
    attempts = 10
elif difficulty == 'hard':
    attempts = 5
print(f"You have {attempts} attempts remaining to guess the number")
# TODO: Have user make a guess.
# TODO: Tell the user if the guess is too high, too low, or correct.
# TODO: Tell the user to guess again if incorrect, and subtract a guess from the current total.
# TODO: Once the user runs out of guesses or guesses the correct number, the game ends.
while game_running:
    user_guess = input("Make a guess: ")
    if user_guess == random_number:
        print("You guessed the correct number, you win!")
        game_running = False
    elif user_guess > random_number:
        print("Too high.")
        print("Guess again.")
        attempts -= 1
        print(f"You have {attempts} attempts remaining to guess the number")
    elif user_guess < random_number:
        print("Too low.")
        print("Guess again.")
        attempts -= 1
        print(f"You have {attempts} attempts remaining to guess the number")
    if attempts == 0:
        print("You have run out of guesses, you lose.")
        print(F"The correct number was {random_number}")
        game_running = False
