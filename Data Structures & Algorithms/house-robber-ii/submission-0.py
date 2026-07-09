class Solution:
    def rob(self, nums: List[int]) -> int:
        # circular house robber, what is the base case then?
        # So base case the same but different array
        # One array treats that last house is unavlaible
        # the other treat first house is unavalible
        dp1 = [0] * (len(nums)-1)
        dp2 = [0] * (len(nums)-1)
        if len(nums) <= 2:
            return max(nums)
        
        nums1 = nums[:len(nums)-1]
        nums2 = nums[1:]

        dp1[0], dp1[1] = nums1[0], max(nums1[0], nums1[1])
        dp2[0], dp2[1] = nums2[0], max(nums2[0], nums2[1])

        for i in range(2, len(nums)-1):
            dp1[i] = max(nums1[i]+dp1[i-2], dp1[i-1])
            dp2[i] = max(nums2[i]+dp2[i-2], dp2[i-1])


        return max(dp1[-1], dp2[-1])