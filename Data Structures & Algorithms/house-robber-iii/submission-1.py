# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        noRob, rob = self._helper(root)
        return max(noRob, rob)
    

    def _helper(self, root: Optional[TreeNode]) -> Tuple[int, int]:
        if not root:
            return 0, 0
        
        leftNoRob, leftRob = self._helper(root.left)
        rightNoRob, rightRob = self._helper(root.right)

        return max(leftNoRob, leftRob) + max(rightNoRob, rightRob), root.val + leftNoRob + rightNoRob
