from random import randint
import os
import time


board_1 = []
board_2 = []

for i in range(8):
    board_1.append(["O"] * 8)
    board_2.append(["O"] * 8)

def print_boards(board_1, board_2):
    print("Player 1 Board         Player 2 Board")
    print("  A B C D E F G H      A B C D E F G H")
    for i in range(8):
        row_1 = " ".join(board_1[i])
        row_2 = " ".join(board_2[i])
        print("%d %s ** %d %s" % (i + 1, row_1, i + 1, row_2))

def add_ship(board, x, y):
    board[x][y] = "S"

def place_computer_ships(board):
    ship_count = 0
    while ship_count < 8:
        x = randint(0, 7)
        y = randint(0, 7)
        if board[x][y] == "O":
            add_ship(board, x, y)
            ship_count += 1

print("Player 1, it's your turn to add ships to your board.")
print_boards(board_1, board_2)

# ask player 1 to add ships
ship_count = 0
while ship_count < 8:
    ship_location = input("Enter the location of your ship (e.g. A1): ")
    if len(ship_location) != 2:
        print("Invalid input. Please enter a valid location (e.g. A1).")
        continue
    x = ord(ship_location[0].upper()) - 65
    y = int(ship_location[1]) - 1
    if x < 0 or x > 7 or y < 0 or y > 7:
        print("Invalid location. Please enter a location within the board (A1 to H8).")
        continue
    add_ship(board_1, x, y)
    ship_count += 1
    print_boards(board_1, board_2)

# place computer ships
place_computer_ships(board_2)

# show player 1 the computer's ships
print("\nComputer ships placed on board 2:")
for i in range(8):
    for j in range(8):
        if board_2[i][j] == "S":
            board_2[i][j] = "S"
print_boards(board_1, board_2)

for i in range(8):
    for j in range(8):
        if board_2[i][j] == "S":
            board_2[i][j] = "S"

# start playing
while True:
    # player 1 turn
    print("\nPlayer 1's turn:")
    guess = input("Guess the coordinates of computer's ship (e.g. A1): ")
    x = ord(guess[0].upper()) - 65
    y = int(guess[1]) - 1
    if board_2[x][y] == "S":
        board_2[x][y] = "S"
        print("Hit!")
    else:
        board_2[x][y] = "X"
        print("Miss!")
    print_boards(board_1, board_2)
    # check if player 1 won
    if "S" not in board_2:
        print("Player 1 won the game!")
        break
    # computer turn
    print("\nComputer's turn:")
    x = randint(0, 7)
    y = randint(0, 7)
    if board_1[x][y] == "S":
        board_1[x][y] = "S"
        print("Computer hit!")
    else:
        board_1[x][y] = "X"
        print("Computer missed!")
    print_boards(board_1, board_2)
    # check if computer won
    if "S" not in board_1:
        print("Computer won the game!")
        break
    time.sleep(2)