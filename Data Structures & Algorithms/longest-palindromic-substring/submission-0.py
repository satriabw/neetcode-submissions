class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]
        for length in range(1, len(s)+1):      # length of substring
            for start in range(len(s)):         # start index
                end = start + length - 1        # end index
                if end >= len(s):
                    break
                if end == start:                          # length 1
                    dp[start][end] = True
                elif end - start == 1:                    # length 2
                    dp[start][end] = s[start] == s[end]
                else:
                    dp[start][end] = s[start] == s[end] and dp[start+1][end-1]
                            
        result = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i][j] and (j - i + 1) > len(result):
                    result = s[i:j+1]
        return result