"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        vals = [(i.start, i.end) for i in intervals]
        vals.sort()
        for i in range(1, len(vals)):
            prev_end = vals[i-1][1]
            if vals[i][0] < prev_end:
                return False
            prev_end = vals[i][1]
        return True