"""
Is there a subset of an array of numbers which sums to a target? if so print one of them?
Use dynamic programming
"""


def solve(row, col):
    if col == 0:
        dp[row][col] = True
    elif row == 0:
        if col == arr[0]:
            dp[row][col] = True
        else:
            dp[row][col] = False
    elif col - arr[row] >= 0:
        dp[row][col] = solve(row - 1, col) or solve(row - 1, col - arr[row])
    else:
        dp[row][col] = solve(row - 1, col)
    return dp[row][col]


arr = [2, 3, 7]
target = 9
n = len(arr)
dp = [[None for i in range(target + 1)] for i in range(n)]
dp[0][0] = True
print(solve(n - 1, target))

"""
find subset
"""
subset = []


def sub(row, col, curr_sum):
    if curr_sum == 0:
        return
    if row < 0 or col < 0:
        return
    if dp[row - 1][col]:
        sub(row - 1, col, curr_sum)
    else:
        subset.append(arr[row])
        curr_sum -= arr[row]
        sub(row - 1, col - arr[row], curr_sum)
    return


if dp[n - 1][target]:
    sub(n - 1, target, target)
    print(sorted(subset))
