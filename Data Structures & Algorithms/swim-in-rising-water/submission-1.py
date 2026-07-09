class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Find a path between top left to bottom right 
        # Top left is always 0 and bottom left can be anything
        # so we get the path at least as high as bottom right
        # Can be solved using bfs?

        queue = [(grid[0][0], (0, 0))]
        visited = set()
        ans = grid[0][0]
        while queue:
            height, node = heapq.heappop(queue)
            if node in visited:
                continue
            visited.add(node)
            ans = max(ans, height)

            if node == (len(grid)-1, len(grid[0])-1):
                break

            directions = [(-1, 0), (1, 0), (0, -1), (0,1)] 
            for dr, dc in directions:
                nr, nc = node[0] + dr, node[1] + dc
                if (nr, nc) in visited or nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                    continue
                heapq.heappush(queue, (max(height, grid[nr][nc]), (nr, nc)))
        
        return ans