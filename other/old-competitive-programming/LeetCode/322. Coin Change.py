class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        n = len(coins)
        
        dp = [amount+1 for _ in range (amount+1)]
        
        dp[0] = 0
        
        for value in range (1, amount+1):
            for coin in coins:
                if value-coin >= 0:
                    dp[value] = min(dp[value], 1 + dp[value-coin])
                    

                
        return dp[amount] if dp[amount] != amount+1 else -1