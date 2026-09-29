class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Idea is to sort intervals first by the start
        # Now we can check with the start interval
        # If next.start <= curr.end, this overlapping, then curr.end become
        # max(next.end, curr.end), else it is not overlapping
        # Then we create new interval
        intervals.sort()
        curr = intervals[0]
        res = []

        for i in range(1, len(intervals)):
            interval = intervals[i]
            # Check overlap
            if interval[0] <= curr[1]:
                curr[1] = max(interval[1], curr[1])
            else:
                res.append(curr)
                curr = interval

        res.append(curr)
        return res