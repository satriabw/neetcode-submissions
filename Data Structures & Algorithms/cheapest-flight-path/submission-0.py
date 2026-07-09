class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # It is like dijkstra but with caveat, that we need max hop to the source. So if the min cost exceeding max hop 
        # We need to backtrack to pick another source

        graph = defaultdict(list)
        visited = defaultdict(int)
        for i in range(n):
            visited[i] = float('inf')
        for s, d, c in flights:
            graph[s].append((c, d))
        
        queue = [(0, (src, 0))] # cost, node, hops
        while queue:
            cost, (node, hops) = heapq.heappop(queue)
            if hops > k+1:
                continue
            if node == dst:
                return cost

            if visited[node] <= hops:
                continue
            visited[node] = hops
            for next_cost, neighbor in graph[node]:
                heapq.heappush(queue, (cost+next_cost, (neighbor, hops+1)))
        return -1
        