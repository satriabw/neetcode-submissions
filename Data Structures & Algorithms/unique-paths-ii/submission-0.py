class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Back tracking + dp
        # dp[i] = min(dp[i+1], dp[j-1])
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        dp[1][1] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if obstacleGrid[i-1][j-1] == 1:
                    dp[i][j] = float('-inf')
                else:
                    dp[i][j] = max(dp[i-1][j] + dp[i][j-1], dp[i][j], dp[i-1][j], dp[i][j-1])
        
        return max(dp[m][n], 0)
