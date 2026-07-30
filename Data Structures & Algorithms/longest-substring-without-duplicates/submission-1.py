class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        if len(s) == 0:
            return 0

        i, j = 0, 1
        sub = 1
        res = 1

        seen.add(s[i])
        while j < len(s):
            if s[j] in seen:
                while i != j and s[i] != s[j]:
                    seen.remove(s[i])
                    sub -= 1
                    i += 1
                # found the duplicate move as starting point
                i += 1
                j += 1
            else:
                sub += 1
                res = max(sub, res)
                seen.add(s[j])
                j += 1

        return res
