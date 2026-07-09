class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # Create subset and check palindrme will be brute force idea
        res, part = [], []
        def dfs(j, i):
            if i >= len(s):
                if i == j:
                    res.append(part.copy())
                return

            if self.checkPalindrome(s, j, i):
                part.append(s[j:i+1])
                dfs(i+1, i+1)
                part.pop()
            
            dfs(j, i+1)

        dfs(0, 0)
        return res

    def checkPalindrome(self,s, start, end) -> bool:
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1

        return True
