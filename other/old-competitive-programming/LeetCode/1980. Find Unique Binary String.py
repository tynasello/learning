'''
Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

 

Example 1:

Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct
'''
    
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        '''
        O(n) time complexity
        A unique binary string is created by setting each index i of the string 
        equal to the compliment of nums[i] at index i
        Based on Cantor's diagonal argument
        '''
        n = len(nums)
        bn = ""
        for i,num in enumerate(nums):
            if num[i]=="0":
                compliment = "1"
            else:
                compliment = "0"
            bn+=compliment
        return bn
            