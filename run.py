from pyfiglet import Figlet
import os
import time

def clear_screen():
    """Clears the terminal screen."""
    os.system('clear' if os.name == 'posix' else 'cls')

    """add art graphicsd to the welcome screen """
custom_fig = Figlet(font='rozzo')
print(custom_fig.renderText('Battleship!'))

intro_string = ("War is upon us! Only the strongest can suvive!\n"

"Do you have the skills to defeat your enemy?\n")

for char in intro_string:
    print(char, end="", flush=True)
    time.sleep(0.1)

    """user enters name"""
name = input("What's your name ally? ")

for char in name:
    print(char, end="", flush=True)
    time.sleep(0.1)
    
welcome_string = " Welcome, " + name + "!"

for char in welcome_string:
    print(char, end="", flush=True)
    time.sleep(0.1)

    """pause between new page"""
time.sleep(2) 

clear_screen()

board = []

print (" ", 1,2,3,4,5)


for i in range(5):
    board.append([str(i+1)] + ["0"]*5)

def print_board(board):

    for i in board:
        print(" ".join(i))

print_board(board)
