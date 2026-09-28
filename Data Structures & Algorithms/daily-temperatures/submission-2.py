class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for _ in range(len(temperatures))]
        for idx, temp in enumerate(temperatures):
            while stack:
                if stack[-1][0] >= temp:
                    break
                _, lastIdx = stack.pop()
                res[lastIdx] = idx-lastIdx
            stack.append((temp, idx))
        return res