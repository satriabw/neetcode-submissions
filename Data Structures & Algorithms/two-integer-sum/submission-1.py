class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}
        for i, num in enumerate(nums):
            pair = target - num
            if num in pairs:
                return [pairs[num], i]
            pairs[pair] = i
