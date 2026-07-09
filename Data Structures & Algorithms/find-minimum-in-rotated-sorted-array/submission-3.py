class Solution:
    def findMin(self, nums: List[int]) -> int:
        mini = float('inf')
        for num in nums:
            mini = min(mini, num)
        
        return mini
        # def searchHelper(nums: List[int], left: int, right: int, curr_min: int) -> int:     
        #     if nums[left] < nums[right] or (left == right):
        #         return min(curr_min, nums[left])
            
        #     mid = (left + right) // 2
        #     curr_min = min(curr_min, nums[mid])
        #     if nums[mid] >= nums[left]:
        #         return searchHelper(nums, mid+1, right, curr_min)
        #     else:
        #         return searchHelper(nums, left, mid-1, curr_min)
        
        # return searchHelper(nums, 0, len(nums)-1, float('inf'))
        
