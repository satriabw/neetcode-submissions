class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums) - 2  # subtract 2 for padding
        dp = [[0] * (n+2) for _ in range(n+2)]
        for length in range(1, n+1):
            for i in range(1, n-length+2):
                j = i + length - 1
                for k in range(i, j+1):
                    dp[i][j] = max((nums[i-1] * nums[k] * nums[j+1]) + dp[i][k-1] + dp[k+1][j], dp[i][j])
    
        return dp[1][n]