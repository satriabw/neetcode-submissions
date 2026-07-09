class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # For graph to be valid tree => all nodes except parents need to hvae a parent
        # A node cannot have two parents -> No cycle in the graph
        # No orphan node, all need to be connected in the tree
        # Algorithm is to detect cycle, after that check if all node is visited

        graph = {}
        visited = [False] * n
        for i in range(n):
            graph.setdefault(i, [])

        for edge in edges: 
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        from collections import deque
        queue = deque([(list(graph.keys())[0], -1)])

        count = 0
        while queue:
            node, parent = queue.popleft()
            visited[node] = True
            count += 1

            for neigh in graph[node]:
                if not visited[neigh]:
                    queue.append((neigh, node))
                elif neigh != parent:
                    return False

        return count == n