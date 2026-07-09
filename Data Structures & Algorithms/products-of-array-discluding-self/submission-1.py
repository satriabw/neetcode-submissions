class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 for i in range(len(nums))]
        postfix = [1 for i in range(len(nums))]
        prefix[0] = nums[0]
        postfix[-1] = nums[-1]

        i = 1
        j = len(nums) - 2
        while i < len(nums) and j >= 0:
            prefix[i] = nums[i] * prefix[i-1]
            postfix[j] = nums[j] * postfix[j+1]

            j -= 1
            i += 1
    
        result = []
        for i in range(len(nums)):
            pre = 1 if i == 0 else prefix[i-1]
            post = 1 if i >= len(nums)-1 else postfix[i+1]

            result.append(pre*post)

        return result
