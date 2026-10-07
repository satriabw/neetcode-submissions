# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxValue = float('-inf')
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def dfs(root: Optional[TreeNode]):
            if not root:
                return 0
            
            leftSum = max(0, dfs(root.left))
            rightSum = max(0, dfs(root.right))
            
            # Calculate max
            self.maxValue = max(self.maxValue, root.val + leftSum + rightSum)

            return root.val + max(leftSum, rightSum)
        
        dfs(root)
        return self.maxValue
        