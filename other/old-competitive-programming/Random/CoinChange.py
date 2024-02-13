"""
Given an amount and the denominations of coins available, determine how many ways change can be made for amount. 
There is a limitless supply of each coin type.
Sample Input 
4 3
1 2 3
Sample Output 
4
"""


def solve(coins, dp, row, col):
    if col == 0:
        res = 1
    elif row <= 0 or col < 0:
        return 0
    elif dp[row][col] != "_":
        res = dp[row][col]
    else:
        take = solve(coins, dp, row, col - coins[row - 1])
        dontTake = solve(coins, dp, row - 1, col)
        res = take + dontTake
    dp[row][col] = res
    return res


if __name__ == "__main__":
    amm, numCoins = map(int, input().split())
    coins = list(map(int, input().split()))
    dp = [["_" for _ in range(amm + 1)] for _ in range(len(coins) + 1)]
    print(solve(coins, dp, len(coins), amm))

"""
4 3
1 2 3
"""