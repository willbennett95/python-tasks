#!/usr/bin/python

from random import randint

board = []


difficulty = int(input("Select difficulty (Easy (1), Medium (2), Hard (3) \n"))

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


def print_board(board):
    print("Battle Area")
    print("===========")
    for row in board:
        print(" ".join(row))


print("                           # #  ( )\n"
              "                        ___#_#___|__\n"
              "                    _  |____________|  _\n"
              "              =====| | |            | | |==== _\n"
              "              =====| |.---------------------------. | |====\n"
"<--------------------'   .  .  .  .  .  .  .  .   '--------------/\n"
 "  \                                                             /\n"
  "   \_________________________BATTLESHIP________________________/")
print("=" * 50)
print("- Take a guess between 0 and 5 for row & column -")
print("- You have " + str(NO_USER_GUESS) + " turns to complete the game -\n")
print("=" * 50 + "\n")
print_board(board)

# find a random integer between 0 and 5 for the row co-ordinate of the battleship
def random_row(board):
    return randint(0, len(board) - 1)


# find a random integer between 0 and 5 for the column co-ordinate of the battleship
def random_col(board):
    return randint(0, len(board[0]) - 1)


ship_row = random_row(board)
ship_col = random_col(board)
turn = 0    # initialise turn to 0 at the start of the game


for attempt in range(NO_USER_GUESS):
    print("\n")
    guess_row = int(input("Guess Row: \n"))
    guess_col = int(input("Guess Col: \n"))

    # if the player guesses correctly, end the game
    if guess_row == ship_row and guess_col == ship_col:
        print("Damn! You sunk my battleship!\n")
        board[guess_row][guess_col] = "✹"
        print_board(board)
        break
    else:
        # if the player enters an invalid co-ordinate, add 1 to turn
        if (guess_row < 0 or guess_row > bounds) or (guess_col < 0 or guess_col > bounds):
            print("Out of bounds!")
        # if the user guesses the same coordinate twice, do nothing
        elif board[guess_row][guess_col] == "◙":
            print("Already Guessed")
        # if the user guesses incorrectly, add 1 to turn
        else:
            print("MISS!")
            board[guess_row][guess_col] = "◙"
        # print the board again showing the missed shot
        print("Turn %d \n" % (turn + 1))
        print_board(board)
        turn = turn + 1
        # if the user hits the predetermined number of guesses, end the game
        if turn == NO_USER_GUESS:
            print("\nGame Over, Better luck next time...")
            board[ship_row][ship_col] = "乂"
            print_board(board)


