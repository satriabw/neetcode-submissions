class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0 for _ in range(n+3)]

        for i in range(n-1, -1, -1):
            val = stoneValue[i] - dp[i+1]
            if i+1 <= n-1:
                val = max((stoneValue[i] + stoneValue[i+1]) - dp[i+2], val)
            if i+2 <= n-1:
                val = max((stoneValue[i] + stoneValue[i+1] + stoneValue[i+2]) - dp[i+3], val)
            dp[i] = val
        
        if dp[0] > 0:
            return "Alice"
        elif dp[0] == 0:
            return "Tie"
        return "Bob"
