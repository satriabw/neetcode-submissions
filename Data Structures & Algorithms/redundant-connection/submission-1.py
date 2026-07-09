class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {}
        indegree = [0] * (len(edges) + 1)
        
        for edge in edges:
            graph.setdefault(edge[0], [])
            graph.setdefault(edge[1], [])

            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

            indegree[edge[0]] += 1
            indegree[edge[1]] += 1

        from collections import deque
        queue = deque([])
        
        for i in range(len(edges)+1):
            if indegree[i] == 1:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            indegree[node] -= 1 # Special case of topo sort
            for neigh in graph[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 1:
                    queue.append(neigh)
        
        print(indegree)
        for u,v in reversed(edges):
            if indegree[u] == 2 and indegree[v]:
                return [u, v]
        
        
        