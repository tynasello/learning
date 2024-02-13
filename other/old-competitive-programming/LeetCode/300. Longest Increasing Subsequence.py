class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * (n)
        # where dp[i] represents the longest increasing
        # subsequence starting at index i of nums

        for starti in range(len(nums) - 1, -1, -1):
            for nexti in range(starti, len(nums)):
                if (nums[starti] < nums[nexti]):
                    dp[starti] = max(dp[starti], 1 + dp[nexti])

        return max(dp)
