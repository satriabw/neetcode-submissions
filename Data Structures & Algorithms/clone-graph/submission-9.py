class Solution:
    def cloneGraph(self, node):
        if node is None:
            return
        

        queue = deque([node])
        copyNode = {node: Node(node.val)}
        visited = set()

        while queue:
            curr = queue.popleft()
            for nei in curr.neighbors:
                if nei not in visited:
                    copyNode[nei] = Node(nei.val)
                    queue.append(nei)
                    visited.add(nei)

                copyNode[curr].neighbors.append(copyNode[nei])
        
        return copyNode[node]
