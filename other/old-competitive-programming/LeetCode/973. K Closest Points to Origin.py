class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        minHeap = []

        for x, y in points:
            proportionalDistFromOrigin = x ** 2 + y ** 2
            heapq.heappush(minHeap, [proportionalDistFromOrigin, x, y])

        res = []

        for _ in range(k):
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])

        return res
