class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # Backtracking so we have target which is nums / 3
        # So given this array should we expand or create new subset
        # If the given subset is not equal k then false

        target = sum(nums) / k
        if target % 1 != 0:
            return False

        nums.sort(reverse=True)
        used = [False] * len(nums)
        def backtrack(i, k, count):
            if k == 0:
                return True
            if count == target:
                return backtrack(0, k-1, 0)
            
            for j in range(i, len(nums)):
                if used[j] or count + nums[j] > target:
                    continue
                used[j] = True
                if backtrack(j+1, k, count+nums[j]):
                    return True
                used[j] = False
            return False
        
        return backtrack(0, k, 0)
