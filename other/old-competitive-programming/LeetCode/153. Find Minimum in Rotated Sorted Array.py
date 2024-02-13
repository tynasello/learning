class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[right] > nums[left]:
                return nums[left]
            middle = left + (right - left) // 2
            if nums[middle] < nums[left]:
                right = middle
            else:
                left = middle + 1

        return nums[left]
