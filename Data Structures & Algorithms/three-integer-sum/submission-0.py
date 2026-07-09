class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array
        # Use two pointers
        # i, l and r
        # if duplicate move the i to the right
        # same with the l

        results = []
        nums.sort()

        for i in range(len(nums) - 2):
            l, r = (i+1, len(nums)-1)
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            while l < r:
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    results.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                
        return results

