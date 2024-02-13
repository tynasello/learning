"""
Total unique ways to make change equal to m
"""


def solve(row, col):
    if col == 0:
        arr[row][col] = 1
    elif row == 0:
        arr[row][col] = 0
    elif col - coins[row - 1] >= 0:
        arr[row][col] = solve(row - 1, col) + solve(row, col - coins[row - 1])
    else:
        arr[row][col] = solve(row - 1, col)
    return arr[row][col]


m = 5
coins = [1, 2, 5]
arr = [[0 for _ in range(m + 1)] for _ in range(len(coins) + 1)]
arr[0][0] = 1
print(solve(len(coins), m))
