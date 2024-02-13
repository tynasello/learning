class Solution:

    def rob(self, nums: List[int]) -> int:
        if (len(nums) == 1):
            return nums[0]
        return max(self.subrob(nums[:-1]), self.subrob(nums[1:]))

    def subrob(self, nums):
        first = 0
        second = 0

        for h in nums:
            temp = max(first+h, second)
            first = second
            second = temp

        return temp
