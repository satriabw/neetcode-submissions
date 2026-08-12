class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        used = [False] * len(nums)
        nums.sort()
        self._helper(nums, [], used, results)
        return results
    

    def _helper(self, nums: List[int], current: List[int], used: List[bool], results: List[List[int]]):
        if len(current) == len(nums):
            results.append(current.copy())
            return

        for i in range(len(nums)):
            if used[i]:
                continue

            if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                continue
            
            current.append(nums[i])
            used[i] = True
            self._helper(nums, current, used, results)
            used[i] = False
            current.pop()
