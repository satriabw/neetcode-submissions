class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for i in range(len(temperatures))]
        stack = []

        for i, temp in enumerate(temperatures):
            
            while len(stack) > 0 and temp > stack[-1][0]:
                _, s_idx = stack.pop()
                result[s_idx] = i - s_idx

            stack.append((temp, i))
        
        return result