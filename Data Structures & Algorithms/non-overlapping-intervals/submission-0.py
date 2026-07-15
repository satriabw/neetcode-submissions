class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort the array
        # Count the number of overlapping interval?
        intervals.sort()
        prev_end = intervals[0][1]
        res = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < prev_end:
                res += 1
                prev_end = min(prev_end, intervals[i][1])
            else:
                prev_end = intervals[i][1]
        return res