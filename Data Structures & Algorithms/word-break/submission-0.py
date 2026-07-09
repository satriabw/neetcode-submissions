class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        dp = [False] * (len(s)+1)
        dp[0] = True
        for j in range(1, len(s)+1):
            dp[j] = any(dp[i] and s[i:j] in words for i in range(j))

        return dp[-1]     