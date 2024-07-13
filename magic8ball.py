# TODO: import random module, and create a file/import that file with the magic 8 ball answers.
import random
from magic8ball_responses import answers
from magic8ball_responses import ascii_art

# TODO: Welcome the user to the game, and prompt them to enter a question to be answered.
# TODO: Find some ASCII art to insert into the project so it shows in the terminal.
print(ascii_art)
print("Welcome to your personal Magic 8 Ball! Shall we begin?")
question = input("What question would you like answered?\n").lower()

# TODO: After user input, print out a 'loading' response from the computer, and then on the next line show response.
print("...Hmm...")
random_answer = random.choice(answers)
print(f"{random_answer}")

# TODO: (EXTRA) - Put in a limit to how many questions the user can ask before the 8 ball gets tired and quits.

# TODO: Add final comments to help with future readability, and shorten/condense code where possible.





