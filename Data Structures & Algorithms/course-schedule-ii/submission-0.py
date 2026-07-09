class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Topo sort again
        graph = {}
        in_degree = [0] * numCourses

        for pre in prerequisites:
            graph.setdefault(pre[1], [])
            graph[pre[1]].append(pre[0])
            in_degree[pre[0]] += 1

        from collections import deque
        queue = deque([])

        for i in range(numCourses):
            graph.setdefault(i, [])
            if in_degree[i] == 0:
                queue.append(i)
        
        result = []

        visit = 0
        visited = set()
        while queue:
            node = queue.popleft()
            if node not in visited:
                result.append(node)
            
            visited.add(node)
            visit += 1
            for neigh in graph[node]:
                in_degree[neigh] -= 1
                if in_degree[neigh] == 0:
                    queue.append(neigh)
        
        return result if visit == numCourses else []