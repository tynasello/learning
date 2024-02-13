class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.m = m
        self.n = n
        self.dp = [[0 for _ in range(n)] for _ in range(m)]
        self.makeMove(0, 0)
        return self.dp[0][0]
    
    def makeMove(self, roboti, robotj):
        if roboti >= self.m or robotj >= self.n:
            return 0

        if roboti == self.m - 1 and robotj == self.n - 1:
            self.dp[roboti][robotj] = 1
            return 1

        # move to right
        if robotj + 1 < self.n and self.dp[roboti][robotj + 1]:
            self.dp[roboti][robotj] += self.dp[roboti][robotj + 1]
        else:
            self.dp[roboti][robotj] += self.makeMove(roboti, robotj + 1)

        # move down    
        if roboti + 1 < self.m and self.dp[roboti + 1][robotj]:
            self.dp[roboti][robotj] += self.dp[roboti + 1][robotj]
        else:
            self.dp[roboti][robotj] += self.makeMove(roboti + 1, robotj)
        
        return self.dp[roboti][robotj]
            