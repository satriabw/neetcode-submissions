# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # two idea is to have root stored as hashmap with the key of the node
        # so we can check from the hash map if the node has common ancestor
        # just to node to construct the hash map, then we reach the targeted q, we can trace if the ancestor exists in node p

        def dfs(root, path, target):
            if not root:
                return (False, path)
            
            if root.val == target.val:
                path.append(target)
                return (True, path)
            
            left = dfs(root.left, path, target)
            right = dfs(root.right, path, target)
            
            if left[0] or right[0]:
                path.append(root)
                return (True, path)
            else:
                return (False, path)
        
        
        _, path_p = dfs(root, [], p)
        _, path_q = dfs(root, [], q)
        if len(path_p) > len(path_q):
            return self.findCommon(path_q, path_p)
        return self.findCommon(path_p, path_q)

    def findCommon(self, a: List[TreeNode], b: List[TreeNode]) -> TreeNode:
        a = a[::-1]
        b = b[::-1]
        lca = a[0]
        for i in range(1, len(a)):
            if a[i].val != b[i].val:
                break
            lca = a[i]
        
        return lca
        