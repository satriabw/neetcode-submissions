class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = 1
        min_prod = 1
        result = float('-inf')
        for i in range(len(nums)):
            max_prod, min_prod = (
                max(nums[i], nums[i]*max_prod, nums[i]*min_prod),
                min(nums[i], nums[i]*max_prod, nums[i]*min_prod)
            )
            result = max(result, max_prod)
        
        return result
        