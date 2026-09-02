class Solution:
    def deleteNode(self, root, key):
        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # found the node to delete
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            # both children exist: find successor, copy value, delete successor
            successor = self._findLeftMost(root.right)
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)

        return root

    def _findLeftMost(self, node):
        while node.left:
            node = node.left
        return node