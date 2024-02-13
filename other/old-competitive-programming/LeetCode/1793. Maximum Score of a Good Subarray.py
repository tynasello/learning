class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:

        # greedy approach - always take largest number to left or right

        left = k
        right = k
        maxScore = nums[k]
        minVal = nums[k]

        while left > 0 or right + 1 < len(nums):

            if left > 0 and right + 1 < len(nums):
                if nums[left - 1] > nums[right + 1]:
                    left -= 1
                    minVal = min(minVal, nums[left])
                else:
                    right += 1
                    minVal = min(minVal, nums[right])

            elif right + 1 < len(nums):
                right += 1
                minVal = min(minVal, nums[right])

            elif left > 0:
                left -= 1
                minVal = min(minVal, nums[left])

            maxScore = max(maxScore, minVal * (right - left + 1))

        return maxScore