
from pyfiglet import Figlet
import os

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

custom_fig = Figlet(font='rozzo')
print(custom_fig.renderText('Battleship!'))

import time

name = input("What's your name? ")

for char in name:
    print(char, end="", flush=True)
    time.sleep(0.1)
    
welcome_string = " Welcome, " + name + "!"

for char in welcome_string:
    print(char, end="", flush=True)
    time.sleep(0.1)

clear_screen()

board = []

print (" ", 1,2,3,4,5)
for i in range(5):
    board.append([str(i+1)] + ["0"]*5)

def print_board(board):
    for i in board:
        print(" ".join(i))

print_board(board)