# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Binary tree is same is the hight of each node is the same
        # And the value is also the same too
        # Flatten it as list an compare?
        # O(n log n + n)

        def dfs(root, res):
            if root and (not root.left and not root.right):
                res.append(root.val)
                return res

            if not root:
                res.append(None)
                return res
            
            res.append(root.val)
            left = dfs(root.left, res)
            right = dfs(root.right, res)

            return res
        
        pList = dfs(p, [])
        qList = dfs(q, [])

        if len(pList) != len(qList):
            return False
        
        return all(x == y for x, y in zip(pList, qList))
