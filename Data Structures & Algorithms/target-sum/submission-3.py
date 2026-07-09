class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        offset = sum(nums)
        if abs(target) > offset:
            return 0
        dp = [[0] * (2 * offset + 1) for _ in range(len(nums))]
        dp[0][+nums[0] + offset] += 1 
        dp[0][-nums[0] + offset] += 1

        for i in range(1, len(nums)):
            for t in range(2 * offset + 1):
                dp[i][t] = 0
                if t - nums[i] >= 0:
                    dp[i][t] += dp[i-1][t - nums[i]]
                if t + nums[i] < 2 * offset + 1:
                    dp[i][t] += dp[i-1][t + nums[i]]
        return dp[len(nums)-1][target + offset]