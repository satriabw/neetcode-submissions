class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # So given word1[0...i] and word2[0...j]
        # How many minimum transformaiton from word1 to word2
        # If they are not same, if they are the same we do not need to do anything
        # we can insert a character, delete or replace
        # how to model these 3 in a dp array?
        # or it does not matter? since it is the same anyway we just need to know
        # we need to perform operation or not
        dp = [[0] * (len(word2)+1) for _ in range(len(word1)+1)]
        
        # Base case to make string become empty string is 1 ops, and it must be non empty string
        for i in range(1, len(word1)+1):
            dp[i][0] = 1 + dp[i-1][0]
        
        # Also base case is empty string word1 to transform to single string word2
        for j in range(1, len(word2)+1):
            dp[0][j] = 1 + dp[0][j-1]
        
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] != word2[j-1]:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                else:
                    dp[i][j] = dp[i-1][j-1]
        
        return dp[len(word1)][len(word2)]