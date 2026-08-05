class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        const = [0] * 3
        for col in nums:
            const[col] += 1
        
        i = 0
        for idx, val in enumerate(const):
            nums[i:i+val] = [idx] * (val)
            i = i + val