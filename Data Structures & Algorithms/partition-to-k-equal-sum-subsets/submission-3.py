class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        target = sum(nums) // k

        nums.sort(reverse=True)
        used = [False] * len(nums)

        def _dfs(i, k, subset):
            if k == 0:
                return True

            if subset == target:
                return _dfs(0, k-1, 0)
            
            for j in range(i, len(nums)):
                # If we have used this element, or if we pick it is more than target just skip
                if used[j] or subset + nums[j] > target:
                    continue
                
                used[j] = True
                if _dfs(j+1, k, subset+nums[j]):
                    return True
                used[j] = False

            return False
        
        return _dfs(0, k, 0)