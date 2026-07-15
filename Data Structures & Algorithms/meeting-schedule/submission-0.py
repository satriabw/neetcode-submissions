"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0:
            return True

        vals = [(i.start, i.end) for i in intervals]
        vals.sort()
        prev_end = vals[0][1]
        for i in range(1, len(vals)):
            if vals[i][0] < prev_end:
                return False
            prev_end = vals[i][1]
        return True