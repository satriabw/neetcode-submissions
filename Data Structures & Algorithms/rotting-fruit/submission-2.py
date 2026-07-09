class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Simple bfs, start from rottent fruit
        # Visit the neighbors from the rotten fruits and add minutes for each visit
        # Then we got the max value of visited fruit
        from collections import deque
        queue = deque([])

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row, col, 0))
        

        result = 0
        visited = set()
        # Bfs part
        while queue:
            row, col, minute = queue.popleft()
            grid[row][col] = 2
            if (row, col) in visited:
                continue

            visited.add((row, col))
            result = max(result, minute)

            for direction in [(-1, 0), (1,0), (0, -1), (0, 1)]:
                nextRow = row+direction[0]
                nextCol = col+direction[1]
                if nextRow >= 0 and nextRow < len(grid) and nextCol >= 0 and nextCol < len(grid[0]) and grid[nextRow][nextCol] == 1:
                    queue.append((nextRow, nextCol, minute+1))
            

        return result if all(grid[r][c] != 1 for r in range(len(grid)) for c in range(len(grid[0]))) else -1
