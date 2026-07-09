class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Solution for this
        # We built empty board at first then we do it recursively
        # Placing the firs Q on 0,0 row, then recursively place queen to 
        # i+1,j+2. The recursively place next to same position but also check board position
        # If it out the bond we rest the position.
        # If it does not satisfy, then we backtrack

        queens = []
        size = n

        def check(i, allPos):
            if i >= size:
                queens.append(allPos[:])
                return
            
            for j in range(size):
                if self.isSafe(allPos, (i, j)):
                    allPos.append((i, j))
                    check(i+1, allPos)
                    allPos.pop()

        check(0, [])
        results = []
        for queen in queens:
            board = [['.' for _ in range(n)] for _ in range(n)]
            for (row, col) in queen:
                board[row][col] = 'Q'

            newBoard = []
            for i in range(n):
                newBoard.append(''.join(board[i]))    
            results.append(newBoard)

        return results

    # Check the diagonal
    def isSafe(self, allPos: List[Tuple[int, int]], currPos: Tuple[int, int]) -> bool:
        for (row, col) in allPos:
            # If in the same colums
            if col == currPos[1]:
                return False
            
            # Check diagonal
            offset = abs(row-currPos[0])
            for i in [1, -1]:
                if col == currPos[1]+(i*offset):
                    return False
        
        return True
