class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Idea is to use indegree instead of visited
        # So we deduct in degree by 1 every time node is visited
        # If it 0, we cannot visit the node again
        # Since it always from jfk, we use min heap with name of the airport as argument
        graph = defaultdict(list)
        for ticket in tickets:
            heapq.heappush(graph[ticket[0]], ticket[1])
        
        result = []
        def dfs(node):
            while graph[node]:
                nextNode = heapq.heappop(graph[node])
                dfs(nextNode)
            result.append(node)

        dfs('JFK')
        return result[::-1]