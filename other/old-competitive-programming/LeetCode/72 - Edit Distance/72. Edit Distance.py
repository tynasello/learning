class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[-1 for _ in range(len(word1) + 1)] for _ in range(len(word2) + 1)]

        def solve(row, col):
            if row == 0 and col == 0:
                return 0
            if row == 0:
                return col
            if col == 0:
                return row
            if dp[row][col] != -1:
                return dp[row][col]
            if word1[col - 1] == word2[row - 1]:
                dp[row][col] = solve(row - 1, col - 1)
            else:
                d = solve(row, col - 1)
                r = solve(row - 1, col - 1)
                i = solve(row - 1, col)
                dp[row][col] = 1 + min(d, r, i)

            return dp[row][col]

        return solve(len(word2), len(word1))
