class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        char = []

        def dfs(left, right):
            if left == right == 0:
                result.append(''.join(char))
                return
            
            if left > 0:
                char.append("(")
                dfs(left-1, right)
                char.pop()
            
            if right > left:
                char.append(")")
                dfs(left, right-1)
                char.pop()
        
        dfs(n, n)
        return result