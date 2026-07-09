class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        
        stack = []
        for c in s:
            if c in pairs:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                pair = stack.pop()
                if pairs[pair] != c:
                    return False
        return True if len(stack) == 0 else False

