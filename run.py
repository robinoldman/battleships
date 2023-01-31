from pyfiglet import Figlet
from random import randint
import os
import time

def clear_screen():
    """Clears the terminal screen."""
    os.system('clear' if os.name == 'posix' else 'cls')
"""
    #add art graphicsd to the welcome screen 
custom_fig = Figlet(font='rozzo')
print(custom_fig.renderText('Battleship!'))

intro_string = ("War is upon us! Only the strongest can suvive!\n"

"Do you have the skills to defeat your enemy?\n")

for char in intro_string:
    print(char, end="", flush=True)
    time.sleep(0.1)

    #user enters name
    
name = input("What's your name ally? ")

for char in name:
    print(char, end="", flush=True)
    time.sleep(0.1)
    
welcome_string = ", Welcome!"

for char in welcome_string:
    print(char, end="", flush=True)
    time.sleep(0.1)

    #pause between new page
time.sleep(2) 
"""
clear_screen()

board = []

print("  1 2 3 4 5")

for i in range(5):
    board.append([str(i+1)] + ["0"]*5)

def print_board(board):
    for i in board:
        print(" ".join(i))

print_board(board)

def computer_row(board):
    return randint(0, len(board)-1)

def computer_col(board):
    return randint(0, len(board[0])-1)

boat_row = computer_row(board)
boat_col = computer_col(board)

while True:
    try:
        player_row = int(input("Guess row:"))
        player_col = int(input("Guess column:"))
        if player_row in range(1, len(board)+1) and player_col in range(1, len(board[0])+1):
            break
        else:
            print("Your input is not within the valid range, please try again.")
    except ValueError:
        print("Your input is not a valid integer, please try again.")

print(boat_row)
print(boat_col)




