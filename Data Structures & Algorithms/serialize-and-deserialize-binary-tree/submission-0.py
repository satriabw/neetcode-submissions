# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ret = ""

        def dfs(root):
            nonlocal ret
            if not root:
                ret += f'n#'
                return
            
            r = f'{root.val}#'
            ret += r

            dfs(root.left)
            dfs(root.right)
            return
        
        dfs(root)
        return ret
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.strip().split("#")[:-1]
        self.idx = 0
        
        def dfs():
            if nodes[self.idx] == 'n':
                self.idx += 1
                return None
            node = TreeNode(int(nodes[self.idx]))
            self.idx += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()     
