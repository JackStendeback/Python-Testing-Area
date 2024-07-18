# TODO: Describe the Problem
# TODO: (What is the for loop doing?) (When is the function meant to print "You got it?") (What is 'i'?)
def my_function():
    for i in range(1, 20):  # This only goes up to 19 correct? Change this to (1, 21)
        if i == 20:
            print("You got it!")


my_function()

# TODO: Reproduce the Bug
from random import randint

dice_imgs = ["1", "2", "3", "4", "5", "6"]  # Error occurs when random picks the number '1'
dice_num = randint(0, 5)  # Error happens when 6 is picked, made the range (0, 5)
print(dice_imgs[dice_num])

# TODO: Play Computer
year = int(input("What's your year of birth?"))
if 1980 < year <= 1994:  # Nothing happens at exactly 1994 when selected. Added '=' to include 1994.
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")

# TODO: Fix the Errors
age = int(input("How old are you?"))  # Converted string into an integer to be used when comparing on the next line.
if age > 18:
    print(f"You can drive at age {age}")  # Made this an f string.

# TODO: Print is Your Friend
# pages = 0 We don't need to declare this if we arent using it before the later lines
# words_per_page = 0 We don't need to declare this yet, has no use case.
pages = int(input("Number of words per page: "))
words_per_page = int(input("Number of words per page: "))
total_words = pages * words_per_page
print(total_words)


# TODO: Use a Debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])
