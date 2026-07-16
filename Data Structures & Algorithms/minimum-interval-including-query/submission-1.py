class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Sort intervals first by start, end -> 
        # For each query in queries, we tried to find in which interval contain the query
        # If we found shortest interval pick it
        
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])
        intervals.sort()
        queries.sort()
        candidates = []
        res = [-1] * len(queries)
        i = 0
        for original_idx, query in sorted_queries:
            while i < len(intervals) and intervals[i][0] <= query:
                length = intervals[i][1] - intervals[i][0] + 1
                heapq.heappush(candidates, (length, intervals[i][1]))
                i += 1
            while candidates and candidates[0][1] < query:
                heapq.heappop(candidates)
            if candidates:
                res[original_idx] = candidates[0][0]

        return res