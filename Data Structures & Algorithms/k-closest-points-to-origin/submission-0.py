class Solution:
    import heapq
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Use min heap to store the point
        # We can use map to map points with the distance

        def distance(x1, x2, y1, y2):
            return (math.sqrt((x1 - x2)**2 + (y1 - y2)**2))
        
        dist = []
        for point in points:
            heapq.heappush(dist, (distance(point[0], 0, point[1], 0), point))

        ret = []
        for i in range(k):
            ret.append(heapq.heappop(dist)[1])
        
        return ret