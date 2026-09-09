class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = set()
        thres = len(nums) / 3
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
            if counter[num] > thres and num not in res:
                res.add(num)
        return list(res)