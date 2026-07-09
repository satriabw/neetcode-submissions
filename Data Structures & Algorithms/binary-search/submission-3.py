class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        mid = len(nums) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            result = self.search(nums[mid + 1:], target)
            return -1 if result == -1 else mid + 1 + result
        else:
            return self.search(nums[:mid], target)