class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = [[0 for _ in range(len(piles))] for _ in range(len(piles))]
        dp[0][0] = piles[0]
        
        self._helper(piles, dp, 0, len(piles)-1)
        return dp[0][len(piles)-1] > 0

    def _helper(self, piles: List[int], dp: List[int][int], left: int, right: int):
        if left > right:
            return 0
        
        if left == right:
            return piles[left]
        
        if dp[left][right] != 0:
            return dp[left][right]

        dp[left][right] = max(piles[left] - self._helper(piles, dp, left+1, right), piles[right] - self._helper(piles, dp, left, right-1))

        return dp[left][right]
