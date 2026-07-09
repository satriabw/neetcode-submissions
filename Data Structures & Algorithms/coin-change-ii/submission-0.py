class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount+1) for _ in range(len(coins))]
        for i in range(len(coins)):
            dp[i][0] = 1
        

        for i in range(len(coins)):
            for t in range(1, amount+1):
                if t >= coins[i]:
                    dp[i][t] = (dp[i-1][t] if i > 0 else 0) + dp[i][t-coins[i]]
                else:
                    dp[i][t] = dp[i-1][t] if i > 0 else 0
        
        return dp[len(coins)-1][amount]