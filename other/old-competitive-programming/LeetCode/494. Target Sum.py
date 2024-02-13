class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = {}

        def dfs(i, currSum):
            if (i, currSum) in dp:
                return dp[(i, currSum)]

            if i == len(nums):
                if currSum == target:
                    return 1
                return 0

            add = dfs(i + 1, currSum + nums[i])
            subtract = dfs(i + 1, currSum - nums[i])
            dp[(i, currSum)] = add + subtract
            return add + subtract

        return dfs(0, 0)
