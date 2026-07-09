class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Start from the edge 'O' to find all valid region, then we can mark it
        # Just to for loop and turn 'O' outside the region as 'X'
        # All 'O' on the edge is the valid region

        visited = set()

        rows, cols = len(board), len(board[0])

        def dfs(row, col, visited):
            if row < 0 or col < 0 or row >= rows or col >= cols or (row, col) in visited or board[row][col] == 'X':
                return
            
            visited.add((row, col))
            dfs(row-1, col, visited)
            dfs(row+1, col, visited)
            dfs(row, col-1, visited)
            dfs(row, col+1, visited)
        
        # Top and bottom row
        for col in range(cols):
            if board[0][col] == 'O':
                dfs(0, col, visited)
            
            if board[rows-1][col] == 'O':
                dfs(rows-1, col, visited)
        
        # Left and right edges
        for row in range(rows):
            if board[row][0] == 'O':
                dfs(row, 0, visited)
            
            if board[row][cols-1] == 'O':
                dfs(row, cols-1, visited)

        
        # Invert the board
        for row in range(1, rows-1):
            for col in range(1, cols-1):
                if board[row][col] == 'O' and (row, col) not in visited:
                    board[row][col] = 'X'
