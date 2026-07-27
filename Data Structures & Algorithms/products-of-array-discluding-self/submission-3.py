class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        
        pref = 1
        for i in range(1, n):
            pref *= nums[i-1]
            res[i] = pref
        
        suf = 1
        for i in range(n-2, -1, -1):
            suf *= nums[i+1]
            res[i] *= suf
        
        return res