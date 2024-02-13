import sys
import math


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [sys.maxsize for _ in range(n + 1)]
        dp[0] = 0

        for sumTo in range(1, n + 1):
            if sqrt(sumTo) == floor(sqrt(sumTo)):
                dp[sumTo] = 1
            for square in range(1, floor(sqrt(sumTo)) + 1):
                dp[sumTo] = min(dp[sumTo], dp[sumTo - square ** 2] + 1)

        return dp[n]