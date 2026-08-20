class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        nums.sort(reverse=True)
        target = total // k
        groups = [0] * k

        def dfs(i):
            if i == len(nums):
                return True
            
            for group in range(k):
                if groups[group] + nums[i] <= target:
                    groups[group] += nums[i]
                    if dfs(i+1):
                        return True
                    groups[group] -= nums[i]
                if groups[group] == 0:
                    break
    
            return False
        
        return dfs(0)