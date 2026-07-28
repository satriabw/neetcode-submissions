class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegrees = {course: 0 for course in range(numCourses)}

        for pre in prerequisites:
            a, b = pre[0], pre[1]
            adj[b].append(a)
            indegrees[a] += 1

        queue = deque([])
        for e, ind in indegrees.items():
            if ind == 0:
                queue.append(e)
        
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            
            for neigh in adj[node]:
                indegrees[neigh] -= 1
                if indegrees[neigh] == 0:
                    queue.append(neigh)
        
        if all(indegrees[i] == 0 for i in range(numCourses)):
            return result
        else:
            return []