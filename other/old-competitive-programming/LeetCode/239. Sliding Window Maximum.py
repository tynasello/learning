class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # append and pop left
        dq = collections.deque([])
        res = []
        left = 0
        right = 0

        while right != len(nums):
            while dq and nums[right] >= nums[dq[-1]]:
                dq.pop()
            dq.append(right)

            # max will be at left most position in deque
            # only append to result if our window spans all of k
            if right >= k - 1:
                res.append(nums[dq[0]])
                left += 1
            right += 1

            # pop numbers that go outside of window
            if dq[0] < left:
                dq.popleft()

        return res
