class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        curr = intervals[0]
        result = []
        for i in range(1, len(intervals)):
            # Merge intervals
            if intervals[i][0] <= curr[1]:
                curr[1] = intervals[i][1] if intervals[i][1] >= curr[1] else curr[1]
            elif intervals[i][0] > curr[1]:
                result.append(curr)
                curr = intervals[i]
                
        result.append(curr)
        return result
