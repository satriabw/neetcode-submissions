"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        queue = deque([(node, None)])
        firstNode = None
        visited = set()
        created = {}

        while queue:
            curr, parent = queue.popleft()
            currCopy = created.setdefault(curr.val, Node(curr.val))
            if parent:
                parent.neighbors.append(currCopy)
                currCopy.neighbors.append(parent)

            if not firstNode:
                firstNode = currCopy
            visited.add(curr)
            
            for neigh in curr.neighbors:
                if neigh in visited:
                    continue
                queue.append((neigh, currCopy))

        return firstNode