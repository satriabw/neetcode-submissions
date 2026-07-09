class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.generateParenthesisHelper(n, 0, 0, [], ans)
        return ans

    def generateParenthesisHelper(self, n: int, left: int, right: int, stack: List[str], ans: List[str]):
        if left == right == n:
            ans.append(''.join(stack))
            return
        
        if left < n:
            stack.append('(')
            self.generateParenthesisHelper(n, left+1, right, stack, ans)
            stack.pop()
        
        if left > right:
            stack.append(')')
            self.generateParenthesisHelper(n, left, right+1, stack, ans)
            stack.pop()
