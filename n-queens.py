def is_safe(board, row, col, n):
    # Check if the current position is safe for the queen
    # Check for the same column
    for i in range(row):
        if board[i][col] == ' Q ':
            return False
    # Check for the upper left diagonal
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == ' Q ':
            return False
        i -= 1
        j -= 1
    # Check for the upper right diagonal
    i = row - 1
    j = col + 1
    while i >= 0 and j < n:
        if board[i][j] == ' Q ':
            return False
        i -= 1
        j += 1
    return True

def solve_n_queens_backtracking(n):
    board = [[' . ' for _ in range(n)] for _ in range(n)]
    solutions = []

    def backtrack(row):
        if row == n:
            solutions.append([' '.join(row) for row in board])
            return
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = ' Q '
                backtrack(row + 1)
                board[row][col] = ' . '
    
    backtrack(0)
    return solutions


def solve_n_queens_branch_and_bound(n):
    board = [[' . ' for _ in range(n)] for _ in range(n)]
    solutions = []

    def place_queen(row):
        if row == n:
            solutions.append([' '.join(row) for row in board])
            return
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = ' Q '
                place_queen(row + 1)
                board[row][col] = ' . '
    
    place_queen(0)
    return solutions







# Test the branch and bound approach
n = 5
solutions = solve_n_queens_branch_and_bound(n)
print("------------------------BRANCH AND BOUND------------------------")
for i, solution in enumerate(solutions):
    print(f"Solution {i+1}:")
    print('--------------------------------------------------------------')
    for row in solution:
        print(row)
    print('--------------------------------------------------------------')


# Test the backtracking approach
n = 5
solutions = solve_n_queens_backtracking(n)
print("------------------------BACKTRACKING------------------------")
for i, solution in enumerate(solutions):
    print(f"Solution {i+1}:")
    print('--------------------------------------------------------------')
    for row in solution:
        print(row)
    print('--------------------------------------------------------------')