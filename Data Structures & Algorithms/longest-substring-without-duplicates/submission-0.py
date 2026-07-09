class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0

        char = set()
        res = 0
        while j < len(s):
            res = max(res, len(char))
            if s[j] not in char:
                char.add(s[j])
                j += 1
            else:
                char.remove(s[i])
                i += 1
        res = max(res, len(char))
        return res