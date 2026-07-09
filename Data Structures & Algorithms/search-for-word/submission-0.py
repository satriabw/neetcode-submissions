class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False] * len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.check(board, i, j, word, "", visited):
                        return True
        return False

    def check(self, board: List[List[str]], row: int, col: int, word:str, curr: str, visited: List[List[bool]]) -> bool:
        if curr == word:
            return True
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or visited[row][col] or len(curr) > len(word) or (curr and curr[-1] != word[len(curr)-1]):
            return False
        
        visited[row][col] = True

        # Start backtrack
        result = self.check(board, row+1, col, word, curr+board[row][col], visited) or self.check(board, row-1, col, word, curr+board[row][col], visited) or self.check(board, row, col+1, word, curr+board[row][col], visited) or self.check(board, row, col-1, word, curr+board[row][col], visited)

        visited[row][col] = False

        return result
