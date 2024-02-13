from sortedcontainers import SortedList


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        n = len(nums)

        sl = SortedList([nums[0]])

        left = 0
        right = 1

        while right != n:
            if (abs(right-left) > indexDiff):
                sl.discard(nums[left])
                left += 1

            if (nums[right] in sl):
                return True

            indexOfClosestToLeft = SortedList.bisect_left(sl, nums[right]) - 1
            indexOfClosestToRight = SortedList.bisect_left(sl, nums[right])

            if abs(sl[indexOfClosestToLeft] - nums[right]) <= valueDiff:
                return True

            if indexOfClosestToRight < len(sl) and abs(sl[indexOfClosestToRight] - nums[right]) <= valueDiff:
                return True

            sl.add(nums[right])
            right += 1

        return False
