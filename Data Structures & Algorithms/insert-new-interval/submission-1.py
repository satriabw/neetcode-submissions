class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Find interval that newInterval part of, if found merge
        # what is interval? because it is sorted, if start of new interval within the interval we need to merge
        # If the start of new interval after the end we can just append the interval
        # If it after, we need to combine the merge and the rest of the interval
        res = []
        for i, interval in enumerate(intervals):
            if newInterval[0] > interval[1]:
                res.append(interval)
            elif newInterval[1] < interval[0]:
                # Append the merge and the rest
                res.append(newInterval)
                res += intervals[i:]
                return res
            else:
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
        res.append(newInterval)
        return res