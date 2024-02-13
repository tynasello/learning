class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        nums.insert(0, 1)
        nums.append(1)
        n = len(nums)

        dp = [[0 for _ in range(n)] for _ in range(n)]

        for windowSize in range(1, n + 1):
            for left in range(n - windowSize + 1):
                right = left + windowSize - 1
                for middle in range(left + 1, right):
                    dp[left][right] = max(
                        dp[left][right],
                        nums[left] * nums[middle] * nums[right]
                        + dp[left][middle]
                        + dp[middle][right],
                    )

        return dp[0][n - 1]
