"""
Your goal is to find the number of ways to construct an array such that consecutive positions contain different values.
Specifically, we want to construct an array with n elements such that each element between 1 and k, inclusive. 
We also want the first and last elements of the array to be 1 and x.

Given n, k and x, find the number of ways to construct such an array. Since the answer may be large, only find it modulo 10^9+7.

For example, for n=4, k=3, x=2, there are 3 ways.
"""


def solve(dp, n, k, x):
    mod = 1000000007
    for i in range(2, n + 1):
        dp[i][1] = (dp[i - 1][2] * (k - 1)) % mod
        dp[i][2] = (dp[i - 1][1] + (dp[i - 1][2] * (k - 2))) % mod
    if x == 1:
        return (k - 1) * dp[i - 1][2] % mod
    else:
        return ((k - 2) * dp[i - 1][2] + dp[i - 1][1]) % mod


if __name__ == "__main__":
    n, k, x = map(int, input().split())
    dp = [[0 for _ in range(3)] for _ in range(n + 1)]
    dp[1][1] = 1
    print(solve(dp, n, k, x))


"""
4 3 2 - 3
1000 100 1 - 43813792
82728 94320 1 - 512473090
942 77 13 - 804842436
"""