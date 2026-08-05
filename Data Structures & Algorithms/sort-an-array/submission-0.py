class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []

        if len(nums) == 1:
            return nums
        
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return self.merge(left, right)
    

    def merge(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1
        
        if j < len(nums2):
            result.extend(nums2[j:])
        else:
            result.extend(nums1[i:])
        
        return result