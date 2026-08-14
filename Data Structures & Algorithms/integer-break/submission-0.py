class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n+1)
        for k in range(2, n+1):
            val = float('-inf')
            for i in range(1, k):
                val = max(val, i*(k-i), dp[k-i]*i)
            dp[k] = val

        return dp[n]