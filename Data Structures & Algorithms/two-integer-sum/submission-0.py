class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevSum = {}
        for i, num in enumerate(nums):
            if num in prevSum:
                return [prevSum[num], i]

            prevSum.setdefault(target-num, i)
        return -1