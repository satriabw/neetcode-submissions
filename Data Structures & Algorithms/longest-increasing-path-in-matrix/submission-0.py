class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
            
        def dfs(i, j):
            if dp[i][j] != 0:
                return dp[i][j]
            dp[i][j] = 1
            for dirI, dirJ in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                neighI = i + dirI
                neighJ = j + dirJ
                if neighI >= 0 and neighI < rows and neighJ >= 0 and neighJ < cols and matrix[neighI][neighJ] > matrix[i][j]:
                    dp[i][j] = max(dp[i][j], 1 + dfs(neighI, neighJ))

            return dp[i][j]

        res = 0
        for row in range(rows):
            for col in range(cols):
                res = max(dfs(row, col), res)
        return  res
            