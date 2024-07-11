# Text Based Adventure Game

def start_game():
    current_room = "starting room"
    game_running = True

    while game_running:
        if current_room == "starting room":
            print("You arrive in a dimly lit room.")
            print("There are doors to the North and to the East.")

            move = input("Which door will you chose? Type north/east/quit\n").lower()
            if move == "north":
                current_room = "intermediate room"
            elif move == "east":
                current_room = "treasure room"
            elif move == "quit":
                game_running = False
                print("Thank you for playing.")
            else:
                print("Invalid move, please try again.")
        elif current_room == "intermediate room":
            print("You arrive in the next room and see a riddle on the wall.")
            print("Solve the riddle to proceed: What fish costs the most?")
            answer = input("Your answer:\n").lower()

            if answer == "goldfish":
                print("Correct! You may now proceed to the next room.")
                current_room = "treasure room"

            else:
                print("Incorrect answer. We will be moving you back to the starting room.")
                current_room = "starting room"

        elif current_room == "treasure room":
            print("Congratulations! You have found the hidden treasure!")
            print("You win!")
            game_running = False


start_game()
