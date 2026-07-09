class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Similar to find min in rotated array
        # First check first if array is rotated
        # If the target is bigger than low nad array rotated then it is in the left
        # Else is in the right
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            if nums[mid] == target:
                return mid
            
            if nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1

        return -1
