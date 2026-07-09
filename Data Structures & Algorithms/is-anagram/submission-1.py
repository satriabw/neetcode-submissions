class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        words = {}
        for c in s:
            words.setdefault(c, 0)
            words[c] += 1
        
        for c in t:
            if c not in words:
                return False
            words[c] -= 1
        
        for _, val in words.items():
            if val > 0:
                return False
        
        return True