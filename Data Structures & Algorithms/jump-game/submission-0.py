class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = nums[0] 
        for i, num in enumerate(nums):
            if i <= max_reach:
                max_reach = max(max_reach, i+nums[i])
            if len(nums)-1 <= max_reach:
                return True
        return False