class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(n, left, right, curr):
            if len(curr) == 2*n:
                res.append(curr)
                return
            
            if left < n:
                backtrack(n, left+1, right, curr+"(")
            
            if right < left:
                backtrack(n, left, right+1, curr+")")
        
        backtrack(n, 0, 0, "")
        return res