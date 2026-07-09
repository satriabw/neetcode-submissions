class Solution:
    def rob(self, nums: List[int]) -> int:
        # We cannot rob adjacent house meaning, house[i-1] and house[i+1] is skipable path
        # The problem is for each house, what is the maximum that we can get?
        # So the base case since we cannot rob adjacent house is in the first two houses?
        # max(house[0], house[1]) => this is the base case
        # if we reach house[2] => only house[0] is good
        # if we reach house[3] => only house[1] is good
        # if we reach house[4] => we add house[2] and current
        if len(nums) <= 2:
            return max(nums)
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])
        
        return dp[-1]

        
        