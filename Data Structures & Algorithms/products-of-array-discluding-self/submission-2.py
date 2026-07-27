class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        pref = 1
        for i in range(1, n):
            pref = pref * nums[i-1]
            res[i] = pref
        
        suff = 1
        for i in range(n-2, -1, -1):
            suff = suff * nums[i+1]
            res[i] *= suff
        
        return res