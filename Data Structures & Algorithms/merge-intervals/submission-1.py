class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Option 1, is to sort the array, based on the start, end
        # then loop it
        # Or we can use a heap? put the array into min heap based on start, end
        # Let's try heap approach
        res = []
        intervals.sort()
        new_interval = [intervals[0][0], intervals[0][1]]
        for i in range(1, len(intervals)):
            # Merge
            if new_interval[1] >= intervals[i][0]:
                new_interval = [min(intervals[i][0], new_interval[0]), max(intervals[i][1], new_interval[1])]
            else:
                res.append(new_interval)
                new_interval = [intervals[i][0], intervals[i][1]]
        res.append(new_interval)
        return res