class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # candidates => contains duplicates
        # target => sum
        # each element can be chosen only one
        # solution set must not contain any combination
        # candidate lengths is 100 => using recursion of 2^n is safe
        '''
        The idea is simple, if we found combination == target we return and add it to solution
        if we decided to pick curr element and it is  > we skip
        We have two options, to include or to not
        '''
        res = []
        candidates.sort()
        self.helper(candidates, target, [], res, 0)
        return res

    
    def helper(self, candidates, target, curr, res, start):
        if target == 0:
            res.append(curr.copy())
            return
        
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue
            
            if candidates[i] > target:
                break

            curr.append(candidates[i])
            self.helper(candidates, target-candidates[i], curr, res, i+1)
            curr.pop()
    