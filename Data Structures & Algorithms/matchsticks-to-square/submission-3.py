class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0:
            return False
        
        sides = [0] * 4
        target = sum(matchsticks) // 4
        matchsticks.sort(reverse=True)
        return self._helper(matchsticks, sides, target, 0)
    
    def _helper(self, matchsticks: List[int], sides: List[int], target:int, i: int) -> bool:
        if i == len(matchsticks):
            return True

        for j in range(4):
            if sides[j] + matchsticks[i] > target:
                continue
            sides[j] += matchsticks[i]
            if self._helper(matchsticks, sides, target, i + 1):
                return True
            sides[j] -= matchsticks[i]

        return False
