class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)  # start with n since range goes 0..n
        for i, num in enumerate(nums):
            result ^= i ^ num
        return result