#!/usr/bin/python

from random import randint

board = []          # initialize the list for the board
NO_USER_GUESS = 0   # defines the number of guesses a user gets depending on the difficulty
bounds = 0          # defines the size of the board depending on difficulty

difficulty = int(input("Select difficulty - Easy (1), Medium (2), Hard (3)\n"))

if difficulty == 1:
    # Number of guesses allowed
    NO_USER_GUESS = 5
    # Create a 4x4 2 dimensional list
    for x in range(4):
        board.append(["○"] * 4)
    bounds = 3

elif difficulty == 2:
    NO_USER_GUESS = 10
    # Create a 5x5 2 dimensional list
    for x in range(5):
        board.append(["○"] * 5)
    bounds = 4

elif difficulty == 3:
    # Number of guesses allowed
    NO_USER_GUESS = 15
    # Create a 6x6 2 dimensional list
    for x in range(6):
        board.append(["○"] * 6)
    bounds = 5


# function to print out the board that will be called after each turn
def print_board():
    print("Battle Area")
    print("===========")
    for y in board:
        print(" ".join(y))

# super cool ascii art for the title of the game
print("                           # #  ( )\n"
              "                        ___#_#___|__\n"
              "                    _  |____________|  _\n"
              "              =====| | |            | | |==== _\n"
              "              =====| |.---------------------------. | |====\n"
"<--------------------'   .  .  .  .  .  .  .  .   '--------------/\n"
 "  \                                                             /\n"
  "   \_________________________BATTLESHIP________________________/")
print("=" * 50)
print("- Take a guess between 0 and ", bounds, "for row & column -")
print("- You have " + str(NO_USER_GUESS) + " turns to complete the game -\n")
print("=" * 50 + "\n")
print_board()


# find a random integer between 0 and 5 for the y  co-ordinate of the battleship
def random_y():
    return randint(0, len(board) - 1)


# find a random integer between 0 and 5 for the column co-ordinate of the battleship
def random_x():
    return randint(0, len(board[0]) - 1)


ship_y = random_y()
ship_x = random_x()
turn = 0    # initialise turn to 0 at the start of the game


for attempt in range(NO_USER_GUESS):
    print("\n")
    guess_y = int(input("Guess Row: \n"))
    guess_x = int(input("Guess Col: \n"))

    # if the player guesses correctly, end the game
    if guess_y  == ship_y  and guess_x == ship_x:
        print("=" * 50 + "\n")
        print("######### Damn! You sunk my battleship! #########\n")
        print("=" * 50 + "\n")
        board[guess_y][guess_x] = "✹"
        print_board()
        break
    else:
        # if the player enters an invalid co-ordinate, add 1 to turn
        if (guess_y < 0 or guess_y > bounds) or (guess_x < 0 or guess_x > bounds):
            print("Out of bounds!")
        # if the user guesses the same coordinate twice, do nothing
        elif board[guess_y][guess_x] == "◙":
            print("Already Guessed")
        # if the user guesses incorrectly, add 1 to turn
        else:
            print("MISS!")
            board[guess_y][guess_x] = "◙"
        # print the board again showing the missed shot
        print("Turn %d \n" % (turn + 1))
        print_board()
        turn = turn + 1
        # if the user hits the predetermined number of guesses, end the game
        if turn == NO_USER_GUESS:
            print("\nGame Over, Better luck next time...\n")
            board[ship_y][ship_x] = "乂"
            print_board()


