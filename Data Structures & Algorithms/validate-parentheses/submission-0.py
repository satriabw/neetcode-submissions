class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        for c in s:
            if c not in {')', ']', '}'}:
                stack.append(c)
            elif not stack:
                return False
            else:
                p = stack.pop()
                if pair[p] != c:
                    return False

        return True if not stack else False
        