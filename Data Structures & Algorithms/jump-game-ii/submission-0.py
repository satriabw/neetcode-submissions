class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_boundary = 0
        max_reach = 0
        for i, num in enumerate(nums):
            if i > current_boundary:
                jumps += 1
                current_boundary = max_reach
            max_reach = max(max_reach, num+i)
        return jumps