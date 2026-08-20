class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        maxVal = 0
        res = 0
        for key, val in count.items():
            if val > maxVal:
                res = key
                maxVal = val
                
        return res
        