"""
Yunjian Lu
Assignment 4 Sudoku
"""


# Takes in 2D List representing the board and outputs it to the console as a sudoku board
def print_sudoku(board):
    if len(board) != 9:
        print("ERROR, Invalid board passed to print_sudoku")
    for row in range(9):
        if len(board[row]) != 9:
            print("ERROR, Invalid board passed to print_sudoku")
        if row % 3 == 0 and row != 0:
            print("---------------------")
        line = ""
        for col in range(9):
            if col % 3 == 0 and col != 0:
                line = line + "| "
            if board[row][col] is None:
                line = line + "* "
            else:
                line = line + str(board[row][col]) + " "
        print(line)


# Takes in 2D List representing the board and returns True if the problem is solved in a valid way
def check_sudoku(board):
    domain = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Check there are no empty cells
    for row in board:
        for col in row:
            if col not in domain:
                return False

    # Check rows for AllDiff
    for row in board:
        if len(row) != len(set(row)):
            return False

    # Check cols for AllDiff
    for i in range(9):
        col = [row[i] for row in board]
        if len(col) != len(set(col)):
            return False

    # Check sub_square for AllDiff
    for i in range(3):
        for j in range(3):
            subsquare = [board[3 * i][3 * j], board[3 * i][3 * j + 1], board[3 * i][3 * j + 2],
                         board[3 * i + 1][3 * j], board[3 * i + 1][3 * j + 1], board[3 * i + 1][3 * j + 2],
                         board[3 * i + 2][3 * j], board[3 * i + 2][3 * j + 1], board[3 * i + 2][3 * j + 2]]
            if len(subsquare) != len(set(subsquare)):
                return False
    return True


# Takes in 2D List representing the board and fills in empty/None squares using AC3
def solve_sudoku(board):
    solved = False
    # on each loop, examine all empty nodes, find all possible values for that node, and fill the node with
    # a value that satisfies all constrains.  Once am empty position is filled, it wont be examine next loop
    while not solved:
        # initialize possible_values to be empty
        possible_values = [[None for _ in range(len(board))] for _ in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] is None:
                    # get all possible values for each empty position in board
                    possible_values[i][j] = get_candidates(i, j, board)
                    # if there is only one possible value for a position, then fill the value in the solution
                    if len(possible_values[i][j]) == 1:
                        board[i][j] = possible_values[i][j][0]

        solved = check_sudoku(board)


# helper method that gets for all possible value in a position( row x and column y)
def get_candidates(x, y, board):

    nums_in_grid = get_nums_in_grid(x, y, board)
    nums_in_col = get_nums_in_col(y, board)

    # to be a candidates, the number satisfies the constrains of there is no same number
    # in the same grid, row, and column
    candidates = [i for i in range(1, len(board) + 1) if i not in board[x]
                  and i not in nums_in_grid and i not in nums_in_col]
    return candidates


# a helper method that gets all numbers in a column
def get_nums_in_col(y, board):
    nums_in_grow = []
    for i in range(len(board)):
        if board[i][y] is not None:
            nums_in_grow.append(board[i][y])
    # print(nums_in_grow)
    return nums_in_grow


# a helper method that gets all numbers in a particular grid
def get_nums_in_grid(x, y, board):
    nums_in_grid = []
    #  if xy is at a grid
    for row in GRIDS:
        if (x, y) in row:
            # get all numbers in that grid
            for ele in row:
                x, y = ele
                if board[x][y] is not None:
                    nums_in_grid.append((board[x][y]))
    # print(nums_in_grid)
    return nums_in_grid


""" 
The GRIDS has 9 lists that represents the 9 different grids(of indexes):
0th list: Up-Left grid, 
1st list: Up- Mid grid, 
2bd list: Up-Right grid, and so on 
"""
GRIDS = [[(0,0), (0,1), (0,2), (1,0), (1,1), (1,2),(2,0), (2,1), (2,2)],
         [(0,3), (0,4), (0,5), (1,3), (1,4), (1,5),(2,3), (2,4), (2,5)],
         [(0,6), (0,7), (0,8), (1,6), (1,7), (1,8),(2,6), (2,7), (2,8)],

         [(3,0), (3,1), (3,2), (4,0), (4,1), (4,2),(5,0), (5,1), (5,2)],
         [(3,3), (3,4), (3,5), (4,3), (4,4), (4,5),(5,3), (5,4), (5,5)],
         [(3,6), (3,7), (3,8), (4,6), (4,7), (4,8),(5,6), (5,7), (5,8)],

         [(6,0), (6,1), (6,2), (7,0), (7,1), (7,2),(8,0), (8,1), (8,2)],
         [(6,3), (6,4), (6,5), (7,3), (7,4), (7,5),(8,3), (8,4), (8,5)],
         [(6,6), (6,7), (6,8), (7,6), (7,7), (7,8),(8,6), (8,7), (8,8)]
         ]


problem1 = [[None, None, 3, None, 2, None, 6, None, None],
            [9, None, None, 3, None, 5, None, None, 1],
            [None, None, 1, 8, None, 6, 4, None, None],
            [None, None, 8, 1, None, 2, 9, None, None],
            [7, None, None, None, None, None, None, None, 8],
            [None, None, 6, 7, None, 8, 2, None, None],
            [None, None, 2, 6, None, 9, 5, None, None],
            [8, None, None, 2, None, 3, None, None, 9],
            [None, None, 5, None, 1, None, 3, None, None]]

problem2 = [[None, 1, 3, 4, 2, None, None, 8, 6],
            [2, None, 4, 6, None, None, None, None, None],
            [None, 8, 7, None, 1, None, 3, None, None],
            [None, None, None, None, 3, None, 6, None, None],
            [None, 6, 2, 5, None, None, None, None, 3],
            [5, None, None, 7, 6, 4, None, 9, 1],
            [7, None, None, None, 4, None, 8, 1, None],
            [None, 4, None, 8, None, None, None, 6, None],
            [None, None, 1, 2, 5, 6, None, 3, 7]]

problem3 = [[6, None, None, None, None, 7, None, 2, None],
            [None, None, None, None, None, None, None, 1, 5],
            [2, 4, 9, None, 1, None, None, None, 3],
            [4, None, 5, 8, None, 1, 3, 9, None],
            [3, 8, None, None, 4, 9, None, None, None],
            [None, 1, 6, None, 7, None, None, None, None],
            [8, None, 4, 1, 5, 3, 6, None, 2],
            [None, None, None, None, 6, 4, 8, 3, None],
            [1, 6, None, None, None, 2, None, None, 9]]
print("Starting:")
print_sudoku(problem1)
solve_sudoku(problem1)
print(check_sudoku(problem1))
# print("solved: ")
print_sudoku(problem1)
print("")

print_sudoku(problem2)
solve_sudoku(problem2)
print(check_sudoku(problem2))
print_sudoku(problem2)
print("")

print_sudoku(problem3)
solve_sudoku(problem3)
print(check_sudoku(problem3))
print_sudoku(problem3)
print("")
