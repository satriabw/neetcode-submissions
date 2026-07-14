class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Find interval that newInterval part of, if found merge
        res = []
        for i, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                res.append(interval)
            elif interval[0] > newInterval[1]:
                res.append(newInterval)
                res += intervals[i:]
                return res
            else:
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
        res.append(newInterval)
        return res