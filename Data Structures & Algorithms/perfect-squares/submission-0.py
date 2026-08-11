class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n+1)

        for i in range(1, n+1):
            val = float('inf')
            for j in range(1, int(math.sqrt(i))+1):
                val = min(val, dp[i-j**2])
            dp[i] = 1 + val
        
        return dp[n]
