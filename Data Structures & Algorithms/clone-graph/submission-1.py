"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        from collections import deque
        # It is adjacency list so use bfs to clone the graph
        visited = set()
        queue = deque([node]) # => (node, parent)
        nodes = {}
        root = node

        while queue:
            node = queue.popleft()
            if not node:
                continue
            visited.add(node)

            if node.val not in nodes:
                nodes[node.val] = Node(node.val, [])

            copyNode = nodes[node.val]
            nodes[copyNode.val] = copyNode

            for neighbor in node.neighbors:
                if neighbor.val not in nodes:
                    nodes[neighbor.val] = Node(neighbor.val, [])
                    queue.append(neighbor)
                copyNode.neighbors.append(nodes[neighbor.val])
                    
        return nodes[root.val] if root else root
        