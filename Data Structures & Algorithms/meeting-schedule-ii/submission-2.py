"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Same idea as removing the overlap but instead removing we take notes
        # How many needed
        intervals.sort(key=lambda x: (x.start, x.end))
        ends = []
        for interval in intervals:
            if ends and interval.start >= ends[0]:
                heapq.heappop(ends)
            heapq.heappush(ends, interval.end)
        return len(ends)