class Solution:
    def trap(self, height: List[int]) -> int:
        # Idea is to find a pair of l <= r
        # We can then calculate the trapping from that
        # Utilize 2 pointers, start from right until r >= l, set as pair
        # if we found better pair replace as max

        max_l, max_r = height[0], height[-1] 
        l, r = 0, len(height) - 1
        count = 0

        while l <= r:
            idx = l if max_l < max_r else r
            count += max(0, min(max_l, max_r) - height[idx])

            if max_l < max_r:
                max_l = max(max_l, height[idx])
                l += 1
            else:
                max_r = max(max_r, height[idx])
                r -= 1

        return count
