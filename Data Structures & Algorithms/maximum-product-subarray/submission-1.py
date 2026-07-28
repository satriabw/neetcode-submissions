class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxValue = nums[0]
        minValue = nums[0]
        result = nums[0]

        for i in range(1, n):
            temp_max = maxValue
            temp_min = minValue

            maxValue = max(nums[i], nums[i]*temp_max, nums[i]*temp_min)
            minValue = min(nums[i], nums[i]*temp_max, nums[i]*temp_min)

            result = max(maxValue, result)
        
        return result