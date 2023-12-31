#!/usr/bin/python3

"""
This program solves the N Queens problem
using backtracking
"""


import sys

solutions = []


def print_board(board):
    """
    print out the NxN board

    params:
    board: a list of list containing integers to represent
    the board

    Returns:
    None
    """
    N = len(board)

    for row in range(N):
        row_buffer = []

        for e in board[row]:
            if e == 0:
                row_buffer.append(" ")
            elif e == 1:
                row_buffer.append("Q")

        print("| {} |".format(" | ".join([e for e in row_buffer])))

        if row != (N - 1):
            print(("|---" * N) + "|")


def print_cords(board):
    N = len(board)
    cords_list = []

    for row in range(N):
        cords_list.append([row, board[row].index(1)])

    print(cords_list)


def checkVaild(board, N, row_pos, col_pos):
    """
    a function to check if the current position
    is not under attack

    board representation for (4x4):
         0 1 2 3
    0 -[[0,0,0,0],
    1 - [0,0,0,0],
    2 - [0,0,0,0],
    3 - [0,0,0,0]]

    params:
    board: a list of lists containing integers to represent
    the N x N board
    N: size of the NxN grid
    row_pos: row position for current cell
    col_pos: column position for current cell

    Returns:
    True if the current cell is a valid non attacking position
    False if the current cell is not a valid non attacking position
    """

    # check columns
    for row in board:
        if row[col_pos] == 1:
            return False

    # check diagonals

    # check upper left
    temp_row_pos, temp_col_pos = row_pos, col_pos

    while temp_row_pos >= 0 and temp_col_pos >= 0:
        if board[temp_row_pos][temp_col_pos] == 1:
            return False
        temp_row_pos -= 1
        temp_col_pos -= 1

    # check lower right
    temp_row_pos, temp_col_pos = row_pos, col_pos

    while temp_row_pos < N and temp_col_pos < N:
        if board[temp_row_pos][temp_col_pos] == 1:
            return False
        temp_row_pos += 1
        temp_col_pos += 1

    # check upper right
    temp_row_pos, temp_col_pos = row_pos, col_pos

    while temp_row_pos >= 0 and temp_col_pos < N:
        if board[temp_row_pos][temp_col_pos] == 1:
            return False
        temp_row_pos -= 1
        temp_col_pos += 1

    # check lower left
    temp_row_pos, temp_col_pos = row_pos, col_pos

    while temp_row_pos < N and temp_col_pos >= 0:
        if board[temp_row_pos][temp_col_pos] == 1:
            return False
        temp_row_pos += 1
        temp_col_pos -= 1

    return True


def find_empty_row(board):
    """
    search for an empty row on the board

    params:
    board: a list of lists containing integers to represent
    the N x N board

    Returns:
    None if no empty rows are found
    an integer representing a row if an empty row is found
    """
    N = len(board)
    for row in range(N):
        if 1 not in board[row]:
            return row
    return None


def backtrack(board, starting_col=0):
    """
    solve the puzzle with backtracking

    params:
    board: a list of lists containing integers to represent
    the N x N board
    starting_col: the index of the first column to check

    Returns:
    True if all rows are filled
    False if a row cannot contain a valid position
    """
    global solutions
    N = len(board)

    # scan for an empty row
    empty_row = find_empty_row(board)

    if empty_row is None:
        board_copy = [[e for e in row] for row in board]
        solutions.append(board_copy)
        return True

    for col in range(starting_col, N):
        if checkVaild(board, N, empty_row, col):
            board[empty_row][col] = 1

            # if there are no more empty rows
            if backtrack(board):
                board[empty_row][col] = 0
                continue

            board[empty_row][col] = 0
    return False


def solve(N):
    """
    initiate the solving process

    params:
    N: size of NxN grid

    Returns:
    None
    """
    # generate board
    board = [[0] * N for i in range(N)]

    backtrack(board)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if N < 4:
        print("N must be at least 4")
        exit(1)

    solve(N)

    for solution in solutions:
        print_cords(solution)

    print("{} solutions".format(len(solutions)))
