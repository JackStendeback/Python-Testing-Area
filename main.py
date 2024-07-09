import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T',
           'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome To The PyPassword Generator!")

# 'int' is converting the user outputs(strings) into usable Integers for the rest of my code
num_of_letters = int(input("How many letters would you like in your password?\n"))
num_of_symbols = int(input("How many symbols would you like?\n"))
num_of_numbers = int(input("How many numbers would you like?\n"))

password_list = []

# Select random letters
for letter in range(num_of_letters):
    password_list.append(random.choice(letters))

# Select random symbols
for symbol in range(num_of_symbols):
    password_list.append(random.choice(symbols))

# Select random numbers
for number in range(num_of_numbers):
    password_list.append(random.choice(numbers))

# Shuffling the letters, numbers and symbols
random.shuffle(password_list)

# Converting the list into a string
password = ''.join(password_list)

print(f"Here is your password: {password}")
