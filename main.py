import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T',
           'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome To The PyPassword Generator!")

num_of_letters = input("How many letters would you like in your password?\n")
num_of_symbols = input("How many symbols would you like?\n")
num_of_numbers = input("How many numbers would you like?\n")

for letter in num_of_letters:
    num_of_letters += 1

for symbol in num_of_symbols:
    num_of_symbols += 1

for number in num_of_numbers:
    num_of_numbers += 1

# print("Here is your password: ")
