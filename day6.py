import random


def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("Welcome to the number guessing game!")
    print(f"Guess the number between 1 and 100. You have {max_attempts} attempts remaining.")

    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts!")
            break

    else:
        print(f"Sorry, you have used all of your attempts. The number to guess was {number_to_guess}")


number_guessing_game()
