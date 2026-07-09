import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # We can use map countring the frequency
        # We can then use the value with heap or similar data structure to get top k
        
        freq = {}
        max_heap = []

        # freq map
        for num in nums:
            freq.setdefault(num, 0)
            freq[num] += 1
        
        top_k = heapq.nlargest(k, freq.items(), key=lambda item: item[1])
        results = [item[0] for item in top_k]
        
        return results

