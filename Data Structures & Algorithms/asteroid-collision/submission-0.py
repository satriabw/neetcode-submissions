class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        result = []
        i = 0

        while i < len(asteroids):
            while stack and i < len(asteroids) and asteroids[i] < 0:
                if stack[-1] < abs(asteroids[i]):
                    stack.pop()
                elif stack[-1] == abs(asteroids[i]):
                    stack.pop()
                    i += 1
                else:
                    i += 1

            if i < len(asteroids):
                if asteroids[i] > 0:
                    stack.append(asteroids[i])
                else:
                    result.append(asteroids[i])
                
            i += 1

        for el in stack:
            result.append(el)

        return result