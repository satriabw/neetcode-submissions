class Solution:
    def countSubstrings(self, s: str) -> int:
        # Use dp table, we can then just count the number of true
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(len(s)):
                start = j
                end = j + i
                if end >= len(s):
                    continue
                if start == end:
                    dp[start][end] = True
                elif (end-start) == 1:
                    dp[start][end] = (s[start] == s[end])
                else:
                    dp[start][end] = (s[start] == s[end]) and (dp[start+1][end-1])
        
        return sum(row.count(True) for row in dp)