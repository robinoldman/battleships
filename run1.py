from random import randint
import os
import time


board_1 = []
board_2 = []

for i in range(8):
    board_1.append(["O"] * 8)
    board_2.append(["O"] * 8)

def print_boards():
    print("Player 1 Board         Player 2 Board")
    print("  A B C D E F G H      A B C D E F G H")
    for i in range(8):
        row_1 = " ".join(board_1[i])
        row_2 = " ".join(board_2[+i])
        print("%d %s ** %d %s" % (i + 1, row_1, i + 1, row_2))

print_boards()