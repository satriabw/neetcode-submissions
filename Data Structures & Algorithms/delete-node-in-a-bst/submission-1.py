# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val == key:
            return self._helper(root)

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)
        return root
    
    def _helper(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        if not node.left and not node.right:
            return None
        if not node.left:
            return node.right
        if not node.right:
            return node.left
        
        sucessor, parent = self._findLeftMost(node.right, node)
        if parent.val != node.val:
            parent.left = sucessor.right
            sucessor.right = node.right
        sucessor.left = node.left

        return sucessor
        

    def _findLeftMost(self, node:Optional[TreeNode], parent: Optional[TreeNode]) -> Tuple[Optional[TreeNode], Optional[TreeNode]]:
        if not node.left:
            return node, parent
        return self._findLeftMost(node.left, node)
