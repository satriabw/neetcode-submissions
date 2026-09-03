class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m-1, n-1
        
        # the idea is to compare position, we know that array is sorted
        # So if we compare: if first array bigger or equal we shift, and move pointer i
        # If array 2 is bigger we move pointer i

        #Shifting right leads to O(N^2), we are not allowed to have enw space
        # instead we know the correct position by adding offset (?)

        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[i+j+1] = nums1[i]
                i -= 1
            else:
                nums1[i+j+1] = nums2[j]
                j -= 1

        while j >= 0:
            nums1[i+j+1] = nums2[j]
            j -= 1