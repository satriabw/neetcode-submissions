"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        size = len(grid[0])
        return self._helper(grid, 0, 0, len(grid[0]))

    def _helper(self, grid: List[List[int]], rowStart: int, colStart: int, size: int) -> Node:
        root = Node()
        if size == 0:
            return

        if all(grid[row][col] == grid[rowStart][colStart] for row in range(rowStart, rowStart+size) for col in range(colStart, colStart+size)):
                root.val = True if grid[rowStart][colStart] else False
                root.isLeaf = True
                return root

        n = size//2
        root.topLeft = self._helper(grid, rowStart, colStart, n)
        root.topRight = self._helper(grid, rowStart, colStart+n, n)
        root.bottomLeft = self._helper(grid, rowStart+n, colStart, n)
        root.bottomRight = self._helper(grid, rowStart+n, colStart+n, n)

        return root