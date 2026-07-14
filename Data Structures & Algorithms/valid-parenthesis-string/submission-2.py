class Solution:
    def checkValidString(self, s: str) -> bool:
        # Standard valid parentheses 
        par = []
        wc = []
        for i, word in enumerate(s):
            if word == '(':
                par.append(i)
            elif word == '*':
                wc.append(i)
            elif word == ')':
                if par:
                    par.pop()
                elif wc:
                    wc.pop()
                else:
                    return False
                    
        while par and wc:
            if par[-1] < wc[-1]: 
                par.pop()
                wc.pop()
            else:
                return False
        
        return len(par) == 0