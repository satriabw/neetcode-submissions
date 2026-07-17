class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        res = []

        while left <= right and top <= bottom:
            # go right along top row
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            top += 1

            # go down along right column
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            # go left along bottom row
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    res.append(matrix[bottom][j])
                bottom -= 1

            # go up along left column
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res