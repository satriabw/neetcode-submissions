class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        queue = deque([node])
        copy = {node: Node(node.val)}

        while queue:
            curr = queue.popleft()
            for nei in curr.neighbors:
                if nei not in copy:
                    copy[nei] = Node(nei.val)
                    queue.append(nei)

                copy[curr].neighbors.append(copy[nei])

        return copy[node]