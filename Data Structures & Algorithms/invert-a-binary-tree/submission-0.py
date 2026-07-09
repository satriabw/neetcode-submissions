# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root = self.invert(root)

        return root
    
    def invert(self, root):
        if not root:
            return 

        left = self.invert(root.left)
        right = self.invert(root.right)

        if root.right and root.left:
            root.right = left
            root.left = right
        elif root.right:
            root.left = right
            root.right = None
        elif root.left:
            root.right = left
            root.left = None

        return root
        
        