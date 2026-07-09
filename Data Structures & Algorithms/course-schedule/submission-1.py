class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}        
        in_degree = [0] * numCourses
        
        for pre in prerequisites:
            graph.setdefault(pre[1], [])

            in_degree[pre[0]] += 1
            graph[pre[1]].append(pre[0])
        
        from collections import deque
        queue = deque([])
        
        for i in range(len(in_degree)):
            graph.setdefault(i, [])
            if in_degree[i] == 0:
                queue.append(i)

        visited = len(in_degree)
        while queue:
            node = queue.popleft()
            
            visited -= 1
            for neigh in graph[node]:
                in_degree[neigh] -= 1
                if in_degree[neigh] == 0:
                    queue.append(neigh)
              
        return visited == 0
