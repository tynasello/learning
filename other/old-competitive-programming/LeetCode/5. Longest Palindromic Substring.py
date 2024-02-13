class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        maxLen = 1
        ans = ""

        for i in range(n):
            dp[i][i] = True
            ans = s[i]

        for end in range(1, n):
            for start in range(end):
                if s[start] == s[end]:
                    if end - start == 1 or dp[start + 1][end - 1]:
                        dp[start][end] = True
                        if end - start + 1 > maxLen and dp[start][end]:
                            maxLen = end - start + 1
                            ans = s[start : end + 1]

        return ans
