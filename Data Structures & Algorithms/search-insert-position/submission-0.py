class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binarySearch(nums: List[int], lo: int, hi: int, target: int) -> int:
            if lo > hi:
                return lo 
            
            mid = (lo+hi) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binarySearch(nums, 0, mid-1, target)
            else:
                return binarySearch(nums, mid+1, hi, target)
        
        idx = binarySearch(nums, 0, len(nums)-1, target)
        return idx
            
