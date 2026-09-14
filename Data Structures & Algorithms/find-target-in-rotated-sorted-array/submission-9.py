class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # so basically we know that array is partially sorted
        # We just need to find where is the part that is sorted
        # Where is the part is not
        # If nums[left] > nums[right] it is rotated, but we still dont know where to move
        

        def binSearch(left, right, target):
            if left > right:
                return -1
            
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    return binSearch(mid+1, right, target)
                return binSearch(0, mid-1, target)
            else:
                if target < nums[mid] or target > nums[right]:
                    return binSearch(0, mid-1, target)
                return binSearch(mid+1, right, target)
        
        return binSearch(0, len(nums)-1, target)