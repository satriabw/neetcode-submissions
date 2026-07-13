class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        total = nums[0]
        for num in nums[1:]:
            total = max(num, total + num)
            best = max(best, total)
        return best