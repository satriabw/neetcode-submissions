class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        return self._helper(nums1, nums2, 0, len(nums1), len(nums1)+len(nums2))
        
    def _helper(self, nums1, nums2, lo, hi, size):
        i = (lo + hi) // 2
        j = (size + 1) // 2 - i

        L1 = float('-inf') if i == 0 else nums1[i-1]
        R1 = float('inf') if i == len(nums1) else nums1[i]
        L2 = float('-inf') if j == 0 else nums2[j-1]
        R2 = float('inf') if j == len(nums2) else nums2[j]

        if L1 > R2:
            return self._helper(nums1, nums2, lo, i-1, size)
        elif L2 > R1:
            return self._helper(nums1, nums2, i+1, hi, size)
        else:
            if size % 2 == 0:
                return (max(L1, L2) + min(R1, R2)) / 2
            else:
                return max(L1, L2)
