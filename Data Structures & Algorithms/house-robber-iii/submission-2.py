# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
    # Basically the idea is we wanted to know the optimum if we decide to rob or not to rob the node and pass it to the parent, and let the parent decide
        def helper(root: Optional[TreenNode]) -> Tuple[int, int]:
            if not root:
                return 0, 0
            
            leftRob, leftNoRob = helper(root.left)
            rightRob, rightNoRob = helper(root.right)

            return root.val + leftNoRob + rightNoRob, max(leftRob, leftNoRob) + max(rightRob, rightNoRob)
    
        rob, noRob = helper(root)
        return max(rob, noRob)