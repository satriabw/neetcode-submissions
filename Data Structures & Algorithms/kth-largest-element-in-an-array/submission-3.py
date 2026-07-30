class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Min heap
        res = []

        for num in nums:
            if len(res) >= k:
                if res[0] >= num:
                    continue
                else:
                    heapq.heappop(res)

            heapq.heappush(res, num)

        return res[0]