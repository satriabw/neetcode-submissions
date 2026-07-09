# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ret = True
    
        def dfs(root):
            nonlocal ret
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            if abs(left-right) > 1:
                ret = False

            return 1 + max(left, right)
        dfs(root)
        return ret