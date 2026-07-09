class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()

        def dfs(grid, row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or (row, col) in visited or grid[row][col] == '0':
                return
            
            visited.add((row, col))

            dfs(grid, row-1, col)
            dfs(grid, row+1, col)
            dfs(grid, row, col-1)
            dfs(grid, row, col+1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(grid, i, j)
                    islands += 1
        
        return islands


[
    ["0","1","0","0","0"],
    ["0","1","0","0","0"],
    ["0","0","1","1","1"],
    ["0","0","0","0","0"]
  ]