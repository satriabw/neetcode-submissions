class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        removeIndex = []
        for i in range(len(nums)):
            if nums[i] == val:
                removeIndex.append(i)
        
        count = 0
        for idx in removeIndex:
            nums.pop(idx-count)
            count += 1
        
        return len(nums)