class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Starting from pacific
        # Starting from atlantic

        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visited, prevHeight):
            if r < 0 or c < 0 or r >= rows or c >= cols or heights[r][c] < prevHeight or (r, c) in visited:
                return
            
            visited.add((r, c))
            dfs(r-1, c, visited, heights[r][c])
            dfs(r+1, c, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
        
        for i in range(cols):
            dfs(0, i, pac, heights[0][i])
            dfs(rows-1, i, atl, heights[rows-1][i])
        
        for j in range(rows):
            dfs(j, 0, pac, heights[j][0])
            dfs(j, cols-1, atl, heights[j][cols-1])
        
        res = []
        for row, col in pac:
            if (row, col) in atl:
                res.append((row, col))
        
        return res