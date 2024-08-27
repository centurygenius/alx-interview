#!/usr/bin/python3
"""
    Backtracking algorithm to place N non-attacking queens 
    on an N×N chessboard.
"""
import sys

def is_safe(board, row, col, n):
    """Check if a queen can be placed on board[row][col]."""
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens_util(board, col, n, solutions):
    """Utilize backtracking to find all solutions."""
    if col >= n:
        solution = []
        for i in range(n):
            row_solution = []
            for j in range(n):
                if board[i][j] == 1:
                    row_solution.append(j)
            solution.append(row_solution)
        solutions.append(solution)
        return True

    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            res = solve_nqueens_util(board, col + 1, n, solutions) or res
            board[i][col] = 0  # backtrack

    return res

def solve_nqueens(n):
    """Solve the N Queens problem."""
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens_util(board, 0, n, solutions)
    return solutions

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

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)

