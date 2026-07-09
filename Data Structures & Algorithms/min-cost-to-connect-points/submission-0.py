class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan(pointI, pointJ):
            xi, yi = pointI
            xj, yj = pointJ
            return abs(xi-xj) + abs(yi-yj)
        
        visited = set()
        queue = [(0, tuple(points[0]))]

        result = 0
        while queue:
            dist, point = heapq.heappop(queue)
            if point in visited:
                continue
            
            visited.add(point)
            result += dist
            for neighPoint in points:
                neighPoint = tuple(neighPoint)
                if neighPoint in visited:
                    continue
                
                nextDist = manhattan(point, neighPoint)
                heapq.heappush(queue, (nextDist, neighPoint))
        return result