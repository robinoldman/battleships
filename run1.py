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
        row_2 = " ".join(board_2[+i])
        print("%d %s ** %d %s" % (i + 1, row_1, i + 1, row_2))

def add_ship(board_1, x, y):
    board_1[x][y] = "S"

print("Player 1, it's your turn to add ships to your board.")
print_boards(board_1, board_2)

ship_count = 0
while ship_count <= 8:
    ship_location = input("Enter the location of your ship (e.g. A1): ")
    # validate input
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
    if ship_count > 8:
        break