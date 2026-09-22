class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')

        i, j = 0, 0
        currSum = 0
        while j <= len(nums):
            if i == j:
                currSum = nums[i] if i < len(nums) else 0
                j += 1

            if currSum >= target:
                ans = min(ans, j-i)
                currSum -= nums[i]
                i += 1
            else:
                currSum += nums[j] if j < len(nums) else 0
                j += 1
                
        return 0 if ans == float('inf') else ans