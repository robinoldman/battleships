"""
1. Show intro message
2. Create two 8x8 boards, where each grid is initialized with the value
"O" indicating that it is unoccupied.

3. Ask player 1 to add ships to their board

4. Place computer ships on board 2

5. Run the game, turn by turn until criteria for game over are met
    Criteria for game over:

6. After game is over, ask player if they want to play again. If so,
run the game again. If not, exit the program.

"""

from random import randint
from pyfiglet import Figlet
import os
import time
import sys

score = 0

#add art graphics to the welcome screen
custom_art = Figlet(font='rozzo')


def clear_screen():
    """
    clears screen
    """
    os.system('clear' if os.name == 'posix' else 'cls')


def slow_type(text, delay=0.1):
    """
    adds slow type to the welcome message
    """
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def print_boards(board_1, board_2):
    """
    Creates board which takes two 2D lists "board_1" and "
    board_2" as arguments.
    """
    print("\n \nPlayer 1 Board         Computer Board")
    print("  A B C D E F G H      A B C D E F G H")
    for i in range(8):
        row_1 = " ".join(board_1[i])
        row_2 = " ".join(board_2[i])
        print("%d %s ** %d %s" % (i + 1, row_1, i + 1, row_2))


def add_ship(board_1, x, y):
        """
        sets the value of the grid in the board at the coordinates x,y to "S".
        """
        board_1[x][y] = "S"


def place_computer_ships(board_2, ship_locations):
    """
    Uses a while loop to run until the count of ships placed
    on the board is equal to 8. In each iteration of the loop, the
    function generates  x and y coordinates using the "randint" function.
    If the grid at the generated coordinates is "O", the code calls the
    "add_ship" function and passes the board. The ship count is then
    increased by 1.
    """
    ship_count = 0
    while ship_count < 8:
        x = randint(0, 7)
        y = randint(0, 7)
        if board_2[x][y] == "O":
            ship_locations.append((x, y))
            ship_count += 1


def play_game():
    """
    Main game
    infinite loop that alternates between the player and computer
    until either the player or the computer wins the game.
    """
    while True:
        # player 1 turn
        print("\nPlayer 1's turn:\n")
        guess = input("Guess the coordinates of the ship (e.g. A1):\n")
        if len(guess) != 2:
            print("Invalid input. Please enter a valid", end=" ")
            print("location (e.g. A1).\n")
            continue
        if not guess[1].isdigit():
            print("Invalid input. Please enter a letter followed", end=" ")
            print("by a number (e.g. A1).\n")
            continue
        y = ord(guess[0].upper()) - 65
        x = int(guess[1]) - 1
        if x < 0 or x > 7 or y < 0 or y > 7:
            print("Invalid location. Please enter a location ", end=" ")
            print("within the board (A1 to H8).\n")
            continue
        if board_2[x][y] != "O":
            print("You have already tried this location. ", end=" ")
            print("Please enter a new location.\n")
            continue

        if (x, y) in ship_locations:
            board_2[x][y] = "H"
            print("Hit!")
        else:
            board_2[x][y] = "M"
            print("Miss!")

        print_boards(board_1, board_2)

        # computer turn
        print("\nComputer's turn:\n")
        x = randint(0, 7)
        y = randint(0, 7)
        if board_1[x][y] == "S":
            board_1[x][y] = "H"
            print("Computer hit!\n")
        else:
            board_1[x][y] = "M"
            print("Computer missed!\n")

        print_boards(board_1, board_2)

        # check if computer won
        if sum([row.count("H") for row in board_1]) == 7:
            print("Computer won the game!\n")
            global computer_score
            computer_score += 1
            print(f"computer score is: {computer_score }\n")
            if input("key Y = new game. Other keys = quit\n").upper() == "Y":
                break
            else:
                print("You have left the game.")
                sys.exit()

        # check if player 1 won
        if sum([row.count("H") for row in board_2]) == 7:
            global score
            print("Player 1 won the game!\n")
            score += 1
            print(f"your score is: {score}\n")

            if input("key Y = new game. Other keys = quit\n").upper() == "Y":
                break
            else:
                print("You have left the game.")
                sys.exit()


print(custom_art.renderText('Battleship!'))

#gives intro to game sets game up for user
intro_string = ("War is upon us! Only the strongest can suvive!\n"
"Do you have the skills to defeat your enemy?\n"
"1. Place your 8 ships in 8 cordinate places\n" 
"2. Guess where the computer has placed it's ships by typing a co-rdinate\n"
"3. For a hit = 'H' for a miss = 'M'\n"
"4. If the computer sinks all 8 of your ships first you loose\n"
"5. If you sink the all 8 of computer's ships you win! \n"
"6. To play again press 'Y' to quit the game press any other button\n")
welcome_string = "Welcome and good luck!"
name = input("What's your name ally? \n")

slow_type(intro_string)
slow_type(name)
slow_type(welcome_string)
time.sleep(2)

#main part of game
while True:
    computer_score = 0
    board_1 = []
    board_2 = []
    ship_locations = []
    ship_count = 0
    used_coordinates = []

    # creates two 8x8 boards, where each grid is initialized with
    # the value "O" indicating that it is unoccupied.
    for i in range(8):
        board_1.append(["O"] * 8)
        board_2.append(["O"] * 8)

    print("Player 1, it's your turn to add ships to your board.")
    print_boards(board_1, board_2)

    # ask player 1 to add ships
    # While loop that runs until the number of ships placed on the
    # board is equal to 8.In each iteration of the loop, code
    # prompts the user to input the location of their ship. If the
    # length of the input is not equal to 2, it prints an error message
    # If the input is valid, the code converts the location to a coordinate
    while ship_count < 8:
        ship_location = input("\nEnter the location of your ship (e.g. A1):")
        if len(ship_location) != 2:
            print("Invalid input. Please enter a valid location (e.g. A1).")
            continue
        if not ship_location[1].isdigit():
            print("Invalid input. Please enter a letter followed", end=" ")
            print("by a number (e.g. A1).\n")
            continue
        y = ord(ship_location[0].upper()) - 65
        x = int(ship_location[1]) - 1
        if x < 0 or x > 7 or y < 0 or y > 7:
            print("Invalid location. Please enter a location.", end=" ")
            print("within the board (A1 to H8).\n")
            continue

        coord = (x, y)
        if coord in used_coordinates:
            print("You have already used that coordinate.", end=" ")
            print("Please enter a different coordinate.\n")
            continue

        used_coordinates.append(coord)
        add_ship(board_1, x, y)
        ship_count += 1
        print_boards(board_1, board_2)

    place_computer_ships(board_2, ship_locations)

    # show player 1 the computer's ships loops over the 8x8 grid of
    # "board_2" to check if each grid contains the character "S". If
    # it does, the grid value is set to "S". calls "print_boards"
    # and passes the two boards, arguments.
    print("\nComputer ships placed on board 2:\n")
    for i in range(8):
        for j in range(8):
            if board_2[i][j] == "S":
                board_2[i][j] = "O"
    print_boards(board_1, board_2)

    play_game()
