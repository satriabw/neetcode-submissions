class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visited = set()

        def dfs(grid, row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or (row, col) in visited or grid[row][col] == 0:
                return 0
            
            visited.add((row, col))
            return grid[row][col] + dfs(grid, row-1, col) + dfs(grid, row+1, col) + dfs(grid, row, col-1) + dfs(grid, row, col+1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    maxArea = max(dfs(grid, i, j), maxArea)
        
        return maxArea

