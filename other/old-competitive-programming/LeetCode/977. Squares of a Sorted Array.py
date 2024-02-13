class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        left, right = 0, n - 1

        while (right - left >= 0):
            if (abs(nums[left]) > abs(nums[right])):
                res[right - left] = nums[left] ** 2
                left += 1
            else:
                res[right - left] = nums[right] ** 2
                right -= 1

        return res

        # n = len(nums)

        # res = []

        # iOfNumClosestToZero = 0

        # i = 1
        # while (i < n and abs(nums[i]) <= abs(nums[i-1])):
        #     iOfNumClosestToZero = i
        #     i += 1

        # res.append(nums[iOfNumClosestToZero] ** 2)
        # left = iOfNumClosestToZero - 1
        # right = iOfNumClosestToZero + 1

        # for _ in range(n - 1):
        #     if (left < 0):
        #         res.append(nums[right] ** 2)
        #         right += 1
        #     elif (right > n - 1):
        #         res.append(nums[left] ** 2)
        #         left -= 1
        #     else:
        #         if (abs(nums[left]) > abs(nums[right])):
        #             res.append(nums[right] ** 2)
        #             right += 1
        #         else:
        #             res.append(nums[left] ** 2)
        #             left -= 1

        # return res
