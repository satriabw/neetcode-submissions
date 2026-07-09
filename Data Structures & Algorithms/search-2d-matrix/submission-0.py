class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Idea is binary search the row => find mid row
        # Check if mid row is within the range, if so perform binary search for that row
        # If not we use binary search row again
        return self.searchRow(matrix, target, 0, len(matrix)-1)


    def searchRow(self, matrix, target, low, hi):
        if low == hi and (target > matrix[low][-1] or target < matrix[low][0]):
            return False

        mid = (hi+low) // 2

        # Found the row
        if target >= matrix[mid][0] and target <= matrix[mid][-1]:
            # Binary search here
            return self.searchColumn(matrix, target, 0, len(matrix[mid])-1, mid)
        elif target > matrix[mid][-1]:
            return self.searchRow(matrix, target, mid+1, hi)
        else:
            return self.searchRow(matrix, target, low, mid)
    
    def searchColumn(self, matrix, target, low, hi, row):
        if low == hi and target != matrix[row][low]:
            return False
        
        mid = (hi + low) // 2
        if target == matrix[row][mid]:
            return True
        elif target > matrix[row][mid]:
            return self.searchColumn(matrix, target, mid+1, hi, row)
        else:
            return self.searchColumn(matrix, target, low, mid, row)

        