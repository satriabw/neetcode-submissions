class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # stores indices
        max_area = 0
        heights.append(0)  # sentinel to flush remaining stack

        for idx, height in enumerate(heights):
            start = idx
            while stack and heights[stack[-1]] > height:
                h = heights[stack.pop()]
                w = idx - (stack[-1] + 1 if stack else 0)
                max_area = max(max_area, h * w)
                start = stack[-1] + 1 if stack else 0
            stack.append(idx)

        return max_area