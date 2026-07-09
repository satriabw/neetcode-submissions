# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.depth(root, 1)
    
    def depth(self, root, depth):
        if not root:
            return depth-1
        
        left = self.depth(root.left, depth+1)
        right = self.depth(root.right, depth+1)

        return max(left, right)