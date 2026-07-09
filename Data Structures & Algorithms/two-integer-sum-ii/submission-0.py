class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def binarySearch(numbers: List[int], left: int, right: int, target: int) -> int:
            if left > right:
                return -1
            
            mid = (left + right) // 2

            if numbers[mid] == target:
                return mid
            
            if target > numbers[mid]:
                return binarySearch(numbers, mid+1, right, target)
            else:
                return binarySearch(numbers, left, mid-1, target)
        
        for i, num in enumerate(numbers):
            pairTarget = target-num
            pairIdx = binarySearch(numbers, 0, len(numbers)-1, pairTarget)
            if pairIdx != -1:
                return [i+1, pairIdx+1]
            
        return -1