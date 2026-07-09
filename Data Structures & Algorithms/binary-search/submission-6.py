class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.searchHelper(nums, target, 0, len(nums)-1)
    
    def searchHelper(self, nums, target, low, hi):
        if low == hi and nums[low] != target:
            return -1
        
        mid = ((hi+low) // 2)

        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            return self.searchHelper(nums, target, mid+1, hi)
        else:
            return self.searchHelper(nums, target, low, mid)
