class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        temp_size = len(temperatures)
        ans = [0 for _ in range(temp_size)]

        for i in range(temp_size):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                prev_temp = stack.pop()
                ans[prev_temp] = i - prev_temp
            
            stack.append(i)
        return ans