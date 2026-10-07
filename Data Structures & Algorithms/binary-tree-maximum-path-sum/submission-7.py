# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode], best: float):
            if not root:
                return 0, best
            
            leftSum, leftBest = dfs(root.left, best)
            rightSum, rightBest = dfs(root.right, best)

            leftSum = max(0, leftSum)
            rightSum = max(0, rightSum)
            
            # Calculate max
            currBest = root.val + leftSum + rightSum

            return root.val + max(leftSum, rightSum), max(currBest, leftBest, rightBest)
        
        _, best = dfs(root, float('-inf'))
        return best
        