import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # We can use map countring the frequency
        # We can then use the value with heap or similar data structure to get top k
        
        freq = {}
        max_heap = []

        # # freq map
        # for num in nums:
        #     freq.setdefault(num, 0)
        #     freq[num] += 1
        
        # top_k = heapq.nlargest(k, freq.items(), key=lambda item: item[1])
        # results = [item[0] for item in top_k]

        # bucket and freq approach
        freq = {}
        max_val = float('-inf')
        for num in nums:
            freq.setdefault(num, 0)
            freq[num] += 1
            max_val = max(max_val, freq[num])

        bucket = [[] for i in range(max_val+1)]
        for key, val in freq.items():
            bucket[val].append(key)
        
        # top k search
        results = []

        i = max_val
        while k > 0 and i >= 0:
            if len(bucket[i]) > 0:
                j = 0
                while k > 0 and j < len(bucket[i]):
                    results.append(bucket[i][j])
                    j += 1
                    k -= 1
            i -= 1

        return results

