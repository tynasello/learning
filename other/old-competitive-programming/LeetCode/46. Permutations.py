class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []

        def permBacktrack(currPerm, inCurrPerm):
            if len(currPerm) == len(nums):
                res.append(currPerm.copy())
                return

            for i, num in enumerate(nums):
                if i in inCurrPerm:
                    continue
                currPerm.append(num)
                inCurrPerm.add(i)
                permBacktrack(currPerm, inCurrPerm)
                inCurrPerm.remove(i)
                currPerm.pop()

        permBacktrack([], set())
        return res
