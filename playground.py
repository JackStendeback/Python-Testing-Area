import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices = ["rock", "paper", "scissors"]

# Rock Paper Scissors
print("Welcome To Rock Paper Scissors!")
user_choice = input("Please select one of the following: 'Rock'. 'Paper'. or 'Scissors'\n").lower()

# User Choice Code
if user_choice == choices[0]:
    print(f"You chose Rock {rock}")
elif user_choice == choices[1]:
    print(f"You chose Paper {paper}")
elif user_choice == choices[2]:
    print(f"You chose Scissors {scissors}")
else:
    print("Invalid choice, please pick between 'Rock', 'Paper' or 'Scissors'")

# Computer Choice Code
computer_choice = random.choice(choices)
if computer_choice == choices[0]:
    print(f"The computer chose Rock {rock}")
elif computer_choice == choices[1]:
    print(f"The computer chose Paper {paper}")
elif computer_choice == choices[2]:
    print(f"The computer chose Scissors {scissors}")
else:
    pass

# Winning / Losing Logic
if user_choice == computer_choice:
    print("It's a tie.")
elif (user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "paper" and computer_choice == "rock") or \
        (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
else:
    print("You lose...")
