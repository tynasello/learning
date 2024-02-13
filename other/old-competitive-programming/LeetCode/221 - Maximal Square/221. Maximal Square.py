class Solution:
    def maximalSquare(self, matrix):
        numR = len(matrix)
        numC = len(matrix[0])

        dp = [[-1 for _ in range(numC)] for _ in range(numR)]

        def solve(row, col):

            if row >= numR or col >= numC:
                return 0

            if dp[row][col] != -1:
                return dp[row][col]

            else:
                toRight = solve(row, col + 1)
                down = solve(row + 1, col)
                downRightDiagonal = solve(row + 1, col + 1)
                if matrix[row][col] == "1":
                    dp[row][col] = 1 + min(toRight, down, downRightDiagonal)
                else:
                    dp[row][col] = 0
            return dp[row][col]

        solve(0, 0)
        maxSquareLen = max(max(l) for l in dp)
        return maxSquareLen ** 2


test1 = Solution
print(
    Solution.maximalSquare(
        None,
        [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ],
    )
)
