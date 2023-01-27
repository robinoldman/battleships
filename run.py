

board = []

    """
    board, row of numbers at the top folowwed by loop of 0s starting with 
    1 and then adding the concecutive number as it goes
    """
print (" ", 1,2,3,4,5)
for i in range(5):
    board.append([str(i+1)] + ["0"]*5)

def print_board(board):
    for i in board:
        print(" ".join(i))

print_board(board)