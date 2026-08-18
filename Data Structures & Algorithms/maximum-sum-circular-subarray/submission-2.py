class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)

        glob_max = nums[0]
        curr_max = nums[0]

        glob_min = nums[0]
        curr_min = nums[0]

        for i in range(1, len(nums)):
            curr_max = max(curr_max + nums[i], nums[i])
            glob_max = max(glob_max, curr_max)

            curr_min = min(curr_min + nums[i], nums[i])
            glob_min = min(glob_min, curr_min)
        
        if (total-glob_min) < glob_max or total==glob_min:
            return glob_max
        else:
            return total-glob_min