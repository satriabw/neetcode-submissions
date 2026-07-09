class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Idenya intinya, ambil mid dari array terkecil
        # Ambil sisanya ke array besar
        # Misal ga memenuhi rightmost partition < leftmost right partition
        # Binary search di array keci


        sizeA = len(nums1)
        sizeB = len(nums2)

        total = sizeA + sizeB
        if total % 2 == 1:
            return self.getKth(nums1, nums2, (total+1) // 2)
        else:
            return (self.getKth(nums1, nums2, total//2) + self.getKth(nums1, nums2, total//2 + 1)) / 2


    def getKth(self, A, B, k):
        # swap
        if len(A) > len(B):
            temp = A
            A = B
            B = temp
        
        if len(A) == 0:
            return B[k-1]
        if k == 1:
            return min(A[0], B[0])
        
        i = min(len(A), k//2)
        j = min(len(B), k//2)

        if A[i-1] <= B[j-1]:
            return self.getKth(A[i:], B, k-i)
        else:
            return self.getKth(A, B[j:], k-j)
            
