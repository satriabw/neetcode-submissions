class MedianFinder:
    import heapq

    def __init__(self):
        self._lo = [] # => max heap
        self._hi = [] # => min heap
        

    def addNum(self, num: int) -> None:
        if len(self._lo) == len(self._hi):
            heapq.heappush_max(self._lo, heapq.heappushpop(self._hi, num))
        else:
            heapq.heappush(self._hi, heapq.heappushpop_max(self._lo, num))

    def findMedian(self) -> float:
        if len(self._lo) != len(self._hi):
            return self._lo[0]
        else:
            return (self._lo[0] + self._hi[0]) / 2
        
        