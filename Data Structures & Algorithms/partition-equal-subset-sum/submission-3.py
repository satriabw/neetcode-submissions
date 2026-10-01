class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Pick or skip, use memo
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        n = len(nums)
        cache = {}

        def dfs(idx, remaining):
            if remaining == 0:
                cache[(idx, remaining)] = True
                return True
            
            if idx == n or remaining < 0:
                cache[(idx, remaining)] = True
                return False
            
            if (idx, remaining) in cache:
                return cache[(idx, remaining)]
            
            res = dfs(idx+1, remaining) or dfs(idx+1, remaining - nums[idx])
            cache[(idx, remaining)] = res
            return res
        
        return dfs(0, target)