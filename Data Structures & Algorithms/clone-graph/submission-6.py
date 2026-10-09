class Solution:
    def cloneGraph(self, node):
        if node is None:
            return None

        copies = {}
        visited = set()
        queue = deque([(node, None)])

        while queue:
            curr, parent_copy = queue.popleft()

            if curr not in copies:
                copies[curr] = Node(curr.val)
            curr_copy = copies[curr]

            # Preserve the edge that brought us here.
            if parent_copy is not None:
                parent_copy.neighbors.append(curr_copy)
                curr_copy.neighbors.append(parent_copy)

            # Incoming edges still count, but explore each node only once.
            if curr in visited:
                continue
            visited.add(curr)

            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    queue.append((neighbor, curr_copy))

        return copies[node]