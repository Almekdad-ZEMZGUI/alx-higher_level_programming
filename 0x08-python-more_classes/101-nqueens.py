#!/usr/bin/python3
"""
101-nqueens module
solves the N queens problem.
"""
import sys


def is_safe(board, row, col, N):
    """
    Check if placing a queen at the specified
    position (row, col) on the board is safe.
    """
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(board, row, N, result):
    """
    Recursively solve the N queens problem using backtracking.
    """
    if row == N:
        queens = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    queens.append([i, j])
        result.append(queens)
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_n_queens(board, row + 1, N, result)
            board[row][col] = 0


def solution(N):
    """
    Print all possible solutions to the N queens
    problem for the given board size N.
    """
    board = [[0] * N for _ in range(N)]
    result = []
    solve_n_queens(board, 0, N, result)
    for sol in result:
        print(sol)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solution(N)
