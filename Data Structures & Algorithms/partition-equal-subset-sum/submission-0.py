class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if (total % 2) > 0:
            return False
        target = total // 2
        dp = [[False] * (target+1) for _ in range(len(nums))]
        dp[0][0] = True
        dp[0][nums[0]] = True
        for i in range(1, len(nums)):
            for t in range(target + 1):
                dp[i][t] = dp[i-1][t] or (dp[i-1][t-nums[i]] if t >= nums[i] else False)

        return dp[len(nums)-1][target]
