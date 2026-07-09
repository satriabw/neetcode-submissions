class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Algorithm is simple
        # Pick current number, then pick it again until invariant is not met
        # If not met we backtrack to pick next number
        # Do over until we found good result

        res = []

        def dfs(i, sub):
            if sum(sub) == target:
                res.append(sub.copy())
                return

            if sum(sub) > target:
                return

            if i >= len(nums):
                return 
            
            sub.append(nums[i])
            dfs(i, sub)
            sub.pop()
            dfs(i+1, sub)
        
        dfs(0, [])
        return res