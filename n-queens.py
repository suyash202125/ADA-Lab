# Function to check if two queens threaten each other or not
def isSafe(board, r, c):
 
    # return false if two queens share the same column
    for i in range(r):
        if board[i][c] == 'Q':
            return False
 
    # return false if two queens share the same `` diagonal
    (i, j) = (r, c)
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i = i - 1
        j = j - 1
 
    # return false if two queens share the same `/` diagonal
    (i, j) = (r, c)
    while i >= 0 and j < len(board):
        if board[i][j] == 'Q':
            return False
        i = i - 1
        j = j + 1
 
    return True
 
#print the board 
def print_board(board):
    for r in board:
        print(str(r).replace(',', '').replace('\'', ''))
    print()
 
 
def SolveNQueens(board, r = 0):
 
    # if `N` queens are placed successfully, print the solution
    if r == len(board):
        print_board(board)
        return
 
    # place queen at every square in the current row `r`
    # and recur for each valid movement
    for i in range(len(board)):
 
        # if no two queens threaten each other
        if isSafe(board, r, i):
            # place queen on the current square
            board[r][i] = 'Q'
 
            # recur for the next row
            SolveNQueens(board, r + 1)
 
            # backtrack and remove the queen from the current square
            board[r][i] = '–'
 
            
#DRIVER CODE
# `N × N` chessboard
N = int(input("Enter the board size: "))

# `board[][]` keeps track of the position of queens in
# the current configuration
board = [['–' for x in range(N)] for y in range(N)]

print(f"\nThe solution {N} X {N} board:")
if N < 4:
    print("No arrange of queens possible.")
else:
    SolveNQueens(board) #FUNCTION CALL