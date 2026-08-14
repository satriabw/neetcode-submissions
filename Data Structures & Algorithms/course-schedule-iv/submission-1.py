class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjGraph = defaultdict(list)
        inDegree = {i : 0 for i in range(numCourses)}

        for (a, b) in prerequisites:
            adjGraph[a].append(b)
            inDegree[b] += 1 
        
        queue = deque([])
        for node in inDegree:
            if inDegree[node] == 0:
                queue.append(node)
        
        reach = defaultdict(set)
        while queue:
            node = queue.popleft()
 
            for neigh in adjGraph[node]:
                inDegree[neigh] -= 1
                if inDegree[neigh] == 0:
                    queue.append(neigh)
                
                reach[neigh] |= reach[node]
                reach[neigh].add(node)
        
        result = []
        for (uj, vj) in queries:
            result.append(uj in reach[vj])
        
        return result