class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        totalsum = sum(nums)
        if (totalsum % 2 != 0):
            return 0
        subsetsum = totalsum / 2

        sums = {0}

        for num in nums:
            temp = set()
            for s in sums:
                if s+num == subsetsum:
                    return 1
                temp.add(s+num)
            sums.update(temp)

        return 0


#         # Brute force. Use dfs -> iterate through number,
#         # at each step put number either into first or second subset
#         # O(2^n) time complexity

#         def dfs(i, sumone, sumtwo):
#             if i == len(nums):
#                 return sumone == sumtwo

#             # add num to first sum
#             if dfs(i+1, sumone+nums[i], sumtwo) == 1:
#                 return 1

#             # add num to second sum
#             if dfs(i+1, sumone, sumtwo+nums[i]) == 1:
#                 return 1


#         return dfs(0, 0, 0)
