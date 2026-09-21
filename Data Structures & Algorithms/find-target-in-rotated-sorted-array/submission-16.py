class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Find the sorted half, check if target within boundaries if not we discard
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # Check which half is rotated
            if nums[left] > nums[mid]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1       # Keep the sorted right half
                else:
                    right = mid - 1      # Keep the rotated left half
            else:
                # It's in this part
                if nums[left] <= target < nums[mid]:
                    right = mid -1 
                else:
                    left = mid + 1
        return -1