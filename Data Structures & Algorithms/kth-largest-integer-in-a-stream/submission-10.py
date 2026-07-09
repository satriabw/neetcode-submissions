class KthLargest:
    import heapq

    def __init__(self, k: int, nums: List[int]):
        self._heap = nums
        heapq.heapify_max(self._heap)
        self._k = k

    def add(self, val: int) -> int:
        heapq.heappush_max(self._heap, val)
        
        res = []
        for i in range(self._k):
            res.append(heapq.heappop_max(self._heap))
        for num in res:
            heapq.heappush_max(self._heap, num)
        return res[self._k-1]
