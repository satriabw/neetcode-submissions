# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Do DFS, but return k - 1 to get k smallest
        # inorder start from left, because the leftmost is the smallest
        count = 0
        def dfs(root, k):
            nonlocal count
            if not root:
                return None

            left = dfs(root.left, k) 
            count += 1
            if count == k:
                return root.val

            right = dfs(root.right, k) 
            return left or right

        return dfs(root, k)