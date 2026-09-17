class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        dup = 1
        for i in range(1, n):
            if nums[i] != nums[i-1]:
                nums[dup] = nums[i]
                dup += 1
        
        return dup