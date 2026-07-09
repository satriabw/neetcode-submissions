class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        result = []

        def dfs(digits, i, part):
            if not digits:
                return
            
            if i >= len(digits):
                result.append(part)
                return
            
            for letter in mapping[digits[i]]:
                dfs(digits, i+1, part+letter)

        dfs(digits, 0, "")
        return result