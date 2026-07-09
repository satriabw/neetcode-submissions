class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Algorithm is we need to have visited array and adjacency list
        # Visit first node in graph first, if not all visited then take first unvisited in array
        visited = [False] * n
        graph = {}
        for i in range(n):
            graph.setdefault(i, [])
        
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        from collections import deque
        def bfs(start):
            queue = deque([start])
            while queue:
                node = queue.popleft()
                visited[node] = True

                for neigh in graph[node]:
                    if not visited[neigh]:
                        queue.append(neigh)
        
        result = 0
        for i in range(n):
            if not visited[i]:
                bfs(i)
                result += 1
        
        return result
            