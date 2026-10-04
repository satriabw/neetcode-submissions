class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # So we can iterate amount from 0..amount, 
        # for every amount, we check for every coin
        #  we check whether for amount-coint there is valid way for every coin
        # we then add this to the dp table, answer will be the dp[amount]
        # base case is to create 0, how many valid way? it is 0
        dp = [-1 for _ in range(amount+1)]
        dp[0] = 0
        for i in range(1, amount+1):
            val = float('inf')
            for coin in coins:
                if coin <= i:
                    val = min(1+dp[i-coin], val)
            dp[i] = val

        return dp[amount] if dp[amount] < float('inf') else -1