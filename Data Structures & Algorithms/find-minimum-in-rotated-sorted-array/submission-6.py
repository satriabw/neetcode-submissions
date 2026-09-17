class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 4 -1 0 1 2 3
        # -1 0 1 2 3 4
        #      mid
        # if left > right rotated and if left > mid, we know we might have something smaller on the left or the mid it self is the smaller, keep the mid as boundary
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2

            if nums[left] > nums[right]:
                # Still rotated
                if nums[left] > nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                return nums[left]

        return nums[left]