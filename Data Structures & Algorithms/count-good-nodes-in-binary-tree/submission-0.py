# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Save the max value for each path
        # In principle, if the node is greater than current max it's the good node
        goodNodes = 0
        def dfs(root, currMax):
            nonlocal goodNodes

            if not root:
                return
            
            if root.val >= currMax:
                goodNodes += 1
            
            dfs(root.left, max(currMax, root.val))
            dfs(root.right, max(currMax, root.val))

            return
        
        dfs(root, float('-inf'))
        return goodNodes