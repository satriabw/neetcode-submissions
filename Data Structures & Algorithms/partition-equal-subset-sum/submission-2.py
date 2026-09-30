class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # In this we do we include this to subset A or not
        # So basically we have allocation sum(nums) // 2 
        # So if we pick this element or skip this element until we reach the allocation
        n = len(nums)
        if sum(nums) % 2 != 0:
            return False

        cache = {}
        def helper(index, remaining):
            if remaining == 0:
                cache[(index, remaining)] = True
                return True
            
            if index == n or remaining < 0:
                cache[(index, remaining)] = False
                return False
            
            if (index, remaining) in cache:
                return cache[(index, remaining)]

            res = helper(index+1, remaining) or helper(index+1, remaining-nums[index])
            cache[(index, remaining)] = res
            return res
        
        remaining = sum(nums) // 2
        return helper(0, remaining)