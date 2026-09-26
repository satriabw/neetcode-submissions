class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Arr is pos and neg
        # smallest missing postive, so search positive el in array, we can disregards if it not positive
        # So find the gap?
        # 00001 xor 00011
        minVal = 1
        maxVal = 0
        
        seen = set()
        for num in nums:
            if num <= 0:
                continue
                
            minVal = min(minVal, num)
            maxVal = max(maxVal, num)
            seen.add(num)
        
        for cdd in range(minVal, maxVal+1):
            if cdd not in seen:
                return cdd
        return maxVal+1