class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # can we model with this: . -> i-1 , for * it 0 or more then i j-1 , exact match i-1 j-1
        dp = [[False] * (len(p)+1) for _ in range(len(s)+1)]
        dp[0][0] = True
        for j in range(1, len(p)+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]

        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] == '*':
                    # We can consume i or zero occurence
                    dp[i][j] = dp[i][j-2] or (dp[i-1][j] if s[i-1] == p[j-2] or p[j-2] == '.' else False)
                elif p[j-1] == '.':
                    # We only consume
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j-1] if s[i-1] == p[j-1] else False
        
        return dp[len(s)][len(p)]