from random import randint
import os
import time


board_1 = []
board_2 = []

#creates two 8x8 boards, where each grid is initialized with 
# the value "O" indicating that it is unoccupied.
for i in range(8):
    board_1.append(["O"] * 8)
    board_2.append(["O"] * 8)

ship_locations = []

# Creates board by which takes two 2D lists "board_1" and "
# board_2" as arguments. The code uses a for loop to iterate 
# over the 8 rows of each board.

def print_boards(board_1, board_2):
    print("Player 1 Board         Player 2 Board")
    print("  A B C D E F G H      A B C D E F G H")
    for i in range(8):
        row_1 = " ".join(board_1[i])
        row_2 = " ".join(board_2[i])
        print("%d %s ** %d %s" % (i + 1, row_1, i + 1, row_2))

#sets the value of the grid in the board at the coordinates x,y to "S".
def add_ship(board_1, x, y):
    board_1[x][y] = "S"

# Uses a while loop to run until the count of ships placed 
# on the board is equal to 8. In each iteration of the loop, the 
# function generates  x and y coordinates using the "randint" function. 
# If the grid at the generated coordinates is "O", the code calls the 
# "add_ship" function and passes the board. The ship count is then 
# increased by 1.
def place_computer_ships(board_2, ship_locations):
    ship_count = 0
    while ship_count < 8:
        x = randint(0, 7)
        y = randint(0, 7)
        if board_2[x][y] == "O":
            ship_locations.append((x, y))
            ship_count += 1

print("Player 1, it's your turn to add ships to your board.")
print_boards(board_1, board_2)

# ask player 1 to add ships
# While loop that runs until the number of ships placed on the 
#board is equal to 8.In each iteration of the loop, code 
#prompts the user to input the location of their ship. If the 
# length of the input is not equal to 2, it prints an error message 
# If the input is valid, the code converts the location to a coordinate

ship_count = 0

while ship_count < 8:
    ship_location = input("Enter the location of your ship (e.g. A1): ")
    if len(ship_location) != 2:
        print("Invalid input. Please enter a valid location (e.g. A1).")
        continue
    y = ord(ship_location[0].upper()) - 65
    x = int(ship_location[1]) - 1
    if x < 0 or x > 7 or y < 0 or y > 7:
        print("Invalid location. Please enter a location within the board (A1 to H8).")
        continue
    add_ship(board_1, x, y)
    ship_count += 1
    print_boards(board_1, board_2)

# place computer ships
place_computer_ships(board_2, ship_locations)


# show player 1 the computer's ships
#loops over the 8x8 grid of "board_2" to check if each 
#grid contains the character "S". If it does, the grid value is set 
# to "S". calls  "print_boards" and passes the two boards, arguments.
print("\nComputer ships placed on board 2:")
for i in range(8):
    for j in range(8):
        if board_2[i][j] == "S":
            board_2[i][j] = "O"
print_boards(board_1, board_2)

#defines the function "play_game()", which implements battleship. 
#infinite loop that alternates between the player and computer 
#until either the player or the computer wins the game.

def play_game():
    while True:
        # player 1 turn
        print("\nPlayer 1's turn:")
        guess = input("Guess the coordinates of computer's ship (e.g. A1): ")
        y = ord(guess[0].upper()) - 65
        x = int(guess[1]) - 1
        if (x, y) in ship_locations:
            board_2[x][y] = "H"
            print("Hit!")
        else:
            board_2[x][y] = "M"
            print("Miss!")
            
        print_boards(board_1, board_2)
        
        # computer turn
        print("\nComputer's turn:")
        x = randint(0, 7)
        y = randint(0, 7)
        if board_1[x][y] == "S":
            board_1[x][y] = "H"
            print("Computer hit!")
        else:
            board_1[x][y] = "X"
            print("Computer missed!")
        
        print_boards(board_1, board_2)
        
        # check if computer won
        if sum([row.count("H") for row in board_1]) == 2:
            print("Computer won the game!")
            break
        
        # check if player 1 won
        if sum([row.count("H") for row in board_2]) == 5:
            print("Player 1 won the game!")
            break



        

play_game()