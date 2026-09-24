TASK 8 – N-QUEEN PROBLEM
Task Name

N-Queen Problem using Backtracking in Python

Problem Statement

Place N queens on an N × N chessboard such that no two queens attack each other. A queen should not be in the same row, column, or diagonal as another queen. The problem is solved using the Backtracking technique.

Code
def is_safe(board, row, col, n):

    for i in range(row):
        if board[i][col] == 1:
            return False

    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve(board, row, n):

    if row == n:
        for r in board:
            print(" ".join("Q" if x else "." for x in r))
        print()
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve(board, row + 1, n)
            board[row][col] = 0


n = int(input("Enter N: "))
board = [[0] * n for _ in range(n)]

solve(board, 0, n)
Output

Input:

Enter N: 4

Output:

. Q . .
. . . Q
Q . . .
. . Q .

Q . . .
. . Q .
. . . Q
. Q . .

Result: The N-Queen problem is successfully solved using Backtracking in Python.
