class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        
        
        n = len(s)
        longestPalindromeLength = 1
        longestPalindromeSubstring = s[0]
        
        dp = [[False for _ in range (n)] for _ in range (n)]
        
        for i in range(n):
            dp[i][i] = True
        
        for right in range(n):
            for left in range (right-1, -1, -1):
                
                if (s[left]==s[right] and (dp[left+1][right-1] or right-left == 1)):    
                        
                        dp[left][right] = True
                        
                        palindrome = s[left:right+1]
                        
                        if len(palindrome) > longestPalindromeLength:    
                            longestPalindromeLength = len(palindrome)
                            longestPalindromeSubstring = palindrome

                
        return longestPalindromeSubstring