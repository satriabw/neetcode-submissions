class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Find if low > hi or now, if it is then array is rotated or part of array rotated
        return self.search(nums, 0, len(nums)-1)
    
    def search(self, nums, low, hi):
        if low >= hi:
            return nums[low]

        mid = (low+hi) // 2

        # If rotated then smaller portion is in the right
        if nums[mid] > nums[hi]:
            return self.search(nums, mid+1, hi)
        else:
            return self.search(nums, low, mid)
