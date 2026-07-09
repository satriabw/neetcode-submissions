class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
            
        dp = [1] * (n)
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n-1]

        # Sub problem so for each steps you pick 1 or 2
        # if steps == n: return 
        # howver to build this we can pick knowledge
        # if we know how much in steps[i], we can just access that
        # return self.helper(0, n)


    def helper(self, steps, n):
        if steps == n:
            return 1
        
        if steps > n:
            return 0

        # Pick one
        return self.helper(steps+1, n) + self.helper(steps+2, n)
        