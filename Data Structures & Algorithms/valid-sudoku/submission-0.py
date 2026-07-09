class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Idea is to have sets = row sets, columns sets, 3x3 sets
        # We can iterate the suduko to check each column, if the element exists on these sets
        # We can assume that the sudoku is invalid

        # we have 9x9
        rows = [set() for i in range(9)]
        columns = [set() for i in range(9)]
        boxes = [[set() for i in range(3)]for j in range(3)]


        for i in range(9):
            for j in range(9):
                # Ignore if it "." 
                if board[i][j] == '.':
                    continue
                    
                # Check the validity of rows and columns and boxes
                if (board[i][j] in rows[j]) or (board[i][j] in columns[i]) or (board[i][j] in boxes[i // 3][j // 3]):
                    return False
                
                # Add to set
                rows[j].add(board[i][j])
                columns[i].add(board[i][j])
                boxes[i // 3][j // 3].add(board[i][j])

        return True
        

    