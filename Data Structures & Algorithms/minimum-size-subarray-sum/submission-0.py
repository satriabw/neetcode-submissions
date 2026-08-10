class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')

        curr = nums[0]
        i, j = 0, 0

        while j <= len(nums):
            if i == j and nums[i] >= target:
                return 1
            
            if curr >= target:
                ans = min(ans, (j-i+1))
                curr -= nums[i]
                i += 1
            else:
                j += 1
                curr += nums[j] if j < len(nums) else 0

        return ans if ans != float('inf') else 0
