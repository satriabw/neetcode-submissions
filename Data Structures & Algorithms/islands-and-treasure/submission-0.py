class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque

        queue = deque([])
        # Find all gates as starting point
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    queue.append((row, col, 0))
        

        # Do BFS, first visited node from the gate guarantees shortest path
        # Do min if overlap
        visited = set()
        while queue:
            row, col, distance = queue.popleft()
            visited.add((row, col))

            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                continue

            if grid[row][col] == 2147483647:
                grid[row][col] = distance
            
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for direction in directions:
                nextRow = row+direction[0]
                nextCol = col+direction[1]
                if (nextRow, nextCol) not in visited and grid[row][col] != -1:
                    queue.append((nextRow, nextCol, distance+1))

