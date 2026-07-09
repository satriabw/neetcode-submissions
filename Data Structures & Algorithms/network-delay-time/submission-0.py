class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        visited = [False] * (n+1)
        for time in times:
            graph.setdefault(time[0], [])
            graph.setdefault(time[1], [])
            graph[time[0]].append((time[2], time[1]))

        queue = [(0, k)]
        result = 0

        while queue:
            weight, node = heapq.heappop(queue)
            if visited[node]:
                continue
            visited[node] = True
            result = weight

            for neigh in graph[node]:
                if visited[neigh[1]]:
                    continue
                heapq.heappush(queue, (neigh[0]+weight, neigh[1]))
        
        return result if all(visited[i] for i in range(1, n+1)) else -1