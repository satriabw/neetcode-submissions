class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Find if the array is rotated or not and check
        # If the target is in the non rotated portion, we could search that, otherwise discard

        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mid = (lo+hi) // 2
            
            if nums[mid] == target:
                return mid
            
            # This part is not rotated
            if nums[lo] <= nums[mid]:
                if target < nums[mid] and target >= nums[lo]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if target > nums[mid] and target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        
        return -1