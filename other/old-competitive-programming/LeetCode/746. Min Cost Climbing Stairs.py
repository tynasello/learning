class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        for i in range(n-2, -1, -1):
            # min cost between one jump and two jumps
            cost[i] += min(cost[i+1], cost[i+2] if i+2 < n else 0)

        return (min(cost[0], cost[1]))


# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:

#         n = len(cost)

#         for i, c in enumerate(reversed(cost[:-1])):
#             i = n-i-2
#             onejump = cost[i+1]
#             twojump = cost[i+2] if i+2 < n else 0
#             cost[i] = c + min(onejump, twojump)

#         return (min(cost[0], cost[1]))
