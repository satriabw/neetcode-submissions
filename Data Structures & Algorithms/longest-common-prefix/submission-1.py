class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]

        mid = len(strs) // 2
        left = self.longestCommonPrefix(strs[:mid])
        right = self.longestCommonPrefix(strs[mid:])

        return self.compare(left, right)

    def compare(self, s1: str, s2: str) -> str:
        min_len = min(len(s1), len(s2))
        for i in range(min_len):
            if s1[i] != s2[i]:
                return s1[:i]
        return s1[:min_len]
