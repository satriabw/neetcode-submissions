class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter.setdefault(num, 0)
            counter[num] += 1
        
        ans = []
        for key, value in sorted(counter.items(), key= lambda item: item[1], reverse=True):
            ans.append(key)
            if len(ans) == k:
                return ans