class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        result = [0]
        # how many ways to reach -2 and 2 values at n-1, sum()
        total = sum(nums)
        dp = [[0 for _ in range(2*total+1)] for _ in range(len(nums))]
        # i => index , j => target, 0 is in the middle (2*total+1)//2 is the sum, index 0 equals -total
        mid = (2*total+1)//2
        dp[0][mid-nums[0]] = 1 # -2, 1 way
        dp[0][mid+nums[0]] += 1 # 2, 1 way

        if abs(target) > total:
            return 0

        for i in range(1, len(nums)):
            for j in range(2*total+1):
                if j + nums[i] < (2*total+1):
                    dp[i][j] += dp[i-1][j+nums[i]]
                if j - nums[i] >= 0:
                    dp[i][j] += dp[i-1][j-nums[i]]

        return dp[len(nums)-1][mid+target]
