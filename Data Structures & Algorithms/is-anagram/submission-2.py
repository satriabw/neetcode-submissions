class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Idea is simple
        # Iterate the both strings with map,
        # If it appears in string s, substract from string t

        if len(s) != len(t):
            return False

        anagram = {}
        for i in range(len(s)):
            anagram.setdefault(s[i], 0)
            anagram.setdefault(t[i], 0)

            anagram[s[i]] += 1
            anagram[t[i]] -= 1
        
        return all(val == 0 for _, val in anagram.items())
        