class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        heights.append(float('-inf'))
        area = float('-inf')

        # Calculate rectangles
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                curr = stack.pop()
                width = i - stack[-1] - 1
                area = max(area, width*heights[curr])

            stack.append(i)
        
        return area
