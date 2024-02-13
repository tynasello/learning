class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        SUM = 0
        for s in stones:
            SUM += s

        dp = [False for _ in range(SUM // 2 + 1)]
        dp[0] = True
        maxSum = 0

        for s in stones:
            temp = dp.copy()
            for after in range(s, SUM // 2 + 1):
                if dp[after - s]:
                    temp[after] = True
                    maxSum = max(maxSum, after)
            dp = temp
        return SUM - maxSum * 2

        # a-b - (c-d)
        # a-b -c+d
        # (a+d) - (b+c)

        # or ((a-b)-c)-d
        # a-b-c-d
        # a-(b+c+d)

        # both scenarios create two sets
        # we need to maximize the second set to minimize the last stone

        # sum = s1+s2
        # ans = s1 - max(s2)
        # ans = sum - s2 - max(s2)
        # ans = sum - 2(max(s2))
