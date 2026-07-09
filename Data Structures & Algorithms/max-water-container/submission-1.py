class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Greedy approach
        left, right = 0, len(heights)-1
        container = float('-inf')
        while left < right:
            height = min(heights[left], heights[right])
            container = max(container, (right-left)*height)

            if heights[right] >= heights[left]:
                left += 1
            else:
                right -= 1
        
        return container