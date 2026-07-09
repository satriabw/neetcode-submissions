class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.generateParenthesisHelper(n, "(", n-1, n, ans)
        return ans

    def generateParenthesisHelper(self, n:int, parenthesis: str, left: int, right:int, combination: List[str]):
        if len(parenthesis) == n*2:
            combination.append(parenthesis)
            return
        
        if left > 0:
            self.generateParenthesisHelper(n, parenthesis+"(", left-1, right, combination)
        
        if left < right:
            self.generateParenthesisHelper(n, parenthesis+")", left, right-1, combination)
