# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Left is the min, so any node in the left should be less than the current min
        # Right is the max, so any node in the right must be more than the current max

        def dfs(root, minVal, maxVal):
            if not root:
                return True
            
            if root.val >= minVal or root.val <= maxVal:
                return False

            return dfs(root.left, min(root.val, minVal), maxVal) and dfs(root.right, minVal, max(root.val, maxVal))
        
        return dfs(root, float('inf'), float('-inf'))
    
