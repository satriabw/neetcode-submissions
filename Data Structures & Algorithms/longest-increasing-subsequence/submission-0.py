class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            dp[i] = 1 + max((dp[j] for j in range(i) if nums[j] < nums[i]), default=0)
        

        return max(dp)
