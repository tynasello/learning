# ---- [ https://leetcode.com/problems/jump-game/ ] ----


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        reach = n - 1

        for i in range(n - 1, -1, -1):
            if (i + nums[i]) >= reach:
                reach = i

        if reach == 0:
            return True
        return False

    # Initial implentation - thought we needed to be able to jump to exactly the last index.
    # def canJump(self, nums: List[int]) -> bool:
    #     n = len(nums)
    #     dp = [False] * n
    #     dp[-1] = True
    #     for start in range(n - 2, -1, -1):
    #         for next in range(1, nums[start] + 1):
    #             if start + next < n and dp[start + next]:
    #                 dp[start] = True
    #                 break
    #
    #     return dp[0]
