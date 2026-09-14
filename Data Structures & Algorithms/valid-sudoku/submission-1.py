class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # We have hash to track columns and rows
        # We have also hash to check mini columns

        # Now the problem is how to iterate the miniboard?
        # Given column + rows we can use to iterate that

        m = len(board)
        n = len(board[0])
        minSize = int(math.sqrt(m))

        rows = [set() for _ in range(m)]
        columns = [set() for _ in range(m)]
        minBoard = [[set() for _ in range(minSize)] for _ in range(minSize)]

        for i in range(m):
            for j in range(n):
                if not board[i][j].isdigit():
                    continue
            
                minBoardI = i // minSize
                minBoardJ = j // minSize
                if board[i][j] in rows[i] or board[i][j] in columns[j] or board[i][j] in minBoard[minBoardI][minBoardJ]:
                    return False
                
                rows[i].add(board[i][j])
                columns[j].add(board[i][j])
                minBoard[minBoardI][minBoardJ].add(board[i][j])
        return True

'''
[
["1","2",".",".","3",".",".",".","."],
["4","3",".","5",".",".",".","5","."],
[".","9","8",".",".",".",".","5","3"],
["5",".",".",".","6",".",".",".","4"],
[".",".",".","8",".","3",".",".","5"],
["7",".",".",".","2",".",".",".","6"],
[".",".",".",".",".",".","2",".","."],
[".",".",".","4","1","9",".",".","8"],
[".",".",".",".","8",".",".","7","9"]
]
'''