class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1

        prefSum = 0
        currCount = 0
        for i in range(0, len(nums)):
            prefSum += nums[i]
            if prefSum-k in prefix:
                currCount += prefix[prefSum-k]
            prefix[prefSum] += 1
        return currCount
        