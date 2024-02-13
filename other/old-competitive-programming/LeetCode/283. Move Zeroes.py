'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:

Input: nums = [0]
Output: [0]

'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        l = 0
        for r in range(len(nums)):
            if nums[r]:
                '''
                swap left and right nums
                if nums[l] is not zero than l and r will be equal
                and the swap will maintain order
                else right will incriment 
                '''
                nums[l],nums[r] = nums[r],nums[l]
                l+=1
        
        return nums
        



# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
        
#         l = 0
#         r = 1
        
#         while r < len(nums):
#             if nums[l] != 0:
#                 l+=1
#                 r=l+1
#             elif nums[r] != 0:
#                 nums[l], nums[r] = nums[r], 0
#                 l+=1
#                 r=l+1
#             else:
#                 r+=1
                
        
#         return nums
        