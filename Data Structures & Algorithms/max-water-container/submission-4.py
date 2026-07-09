class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Idea is using pointer l, r
        # we need to move as long as one is higher, because watter will spill
        # if l > r, r-= else l -=
        # track the maximum water for each movement

        res = float('-inf')
        l, r = 0, len(heights) - 1
        while l < r:
            # calculate water for now
            height = min(heights[l], heights[r])
            width = r - l
            res = max(res, height * width)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return res
