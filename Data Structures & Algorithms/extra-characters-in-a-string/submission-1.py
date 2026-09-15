class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # So the task is to break up character into optimum way
        # So we need to start creating Trie and check if we able to find something
        # So basically we try to do it greeedily
        n = len(s)
        dp = [0] * (n+1)

        for i in range(n-1, -1, -1):
            dp[i] = 1 + dp[i+1]
            for word in dictionary:
                if i + len(word) <= n and s[i:i+len(word)] == word:
                    dp[i] = min(dp[i], dp[i+len(word)])
            
        return dp[0]