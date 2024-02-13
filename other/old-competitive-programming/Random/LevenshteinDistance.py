"""
find the minimal ammoung of operations needed to convert one string into another
you can replace, insert, or delete characters
"""


def solve(row, col):
    if row == 0 and col == 0:
        res = 0
    elif row == 0:
        res = col
    elif col == 0:
        res = row
    elif dp[row][col] != -1:
        res = dp[row][col]
    else:
        if s2[row - 1] == s1[col - 1]:
            res = solve(row - 1, col - 1)
        else:
            delet = solve(row, col - 1)
            insert = solve(row - 1, col)
            replace = solve(row - 1, col - 1)
            res = 1 + min(delet, replace, insert)
    dp[row][col] = res
    return res


s1 = "pairs"
s2 = "cars"

n1 = len(s1)
n2 = len(s2)
dp = [[-1 for i in range(n1 + 1)] for i in range(n2 + 1)]
print(solve(n2, n1))