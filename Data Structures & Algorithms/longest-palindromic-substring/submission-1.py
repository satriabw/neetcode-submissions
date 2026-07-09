class Solution:
    def longestPalindrome(self, s: str) -> str:
        # First we generate the subset of all string with length 1,..,n
        # Idea is build dp table of [start][end]
        # If we expand start-1,end+1 and dp is palindrome, then the string
        # Is also palindrome

        dp =[[False for _ in range(len(s))] for _ in range(len(s))]

        for i in range(1, len(s)+1):
            for j in range(len(s)):
                start = j
                end = j + i - 1 
                if end >= len(s):
                    continue
                if end == start:
                    dp[start][end] = True
                elif (end-start) == 1:
                    dp[start][end] = (s[start] == s[end])
                else:
                    dp[start][end] = (s[start] == s[end]) and (dp[start+1][end-1])
        
        result = ""
        for start in range(len(dp)):
            for end in range(len(dp)):
                if dp[start][end] and len(result) < (end-start+1):
                    result = s[start:end+1]
        return result
                