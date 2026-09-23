# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # left subtree contains only nodes with keys less than node keys
        # right subtree contains only nodes with keys more than node keys
        # both left and right are binary search trees

        # Invariant to see, if a subtree is valid binary search tree deos not mean it will be valid with the parents. Imagine if left.right > than the root or parents, then it wont be valid. 
        # So how to make a valid? Use min and max value -> we cannot break this everytime we going down
        # Going to the left? update min
        # Going to the right update max
        # Node needs to be less than min but bigger than max

        def isValid(root: Optional[TreeNode], minVal: int, maxVal: int) -> bool:
            if not root:
                return True
            
            if root.val >= minVal or root.val <= maxVal:
                return False
            
            return isValid(root.left, min(minVal, root.val), maxVal) and isValid(root.right, minVal, max(root.val, maxVal))
        
        return isValid(root, float('inf'), float('-inf'))
        