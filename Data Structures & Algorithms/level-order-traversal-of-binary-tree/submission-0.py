# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # use inorder traversal, but we pass level (height information) from the root
        # So if it is the root add to the result using the index
        # list is mutable so we can pass as argument in recursive function
        ret = []

        def dfs(root, level):
            nonlocal ret

            if not root:
                return
            
            if len(ret) <= level:
                ret.append([root.val])
            else:
                ret[level].append(root.val)
            
            dfs(root.left, level+1)
            dfs(root.right, level+1)
        
            return
        dfs(root, 0)
        return ret