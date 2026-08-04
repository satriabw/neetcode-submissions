class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Divide and conquer approach
        if len(strs) == 0:
            return ''
        
        if len(strs) == 1:
            return strs[0]
        
        mid = len(strs) // 2
        left = self.longestCommonPrefix(strs[:mid])
        right = self.longestCommonPrefix(strs[mid:])
        
        return self.compare(left, right)

    def compare(self, s1, s2):
        if len(s1) == 0 or len(s2) == 0:
            return ''
        
        res = ''
        while len(s1) > 0 and len(s2) > 0:
            if s1[0] == s2[0]:
                res += s1[0]
                s1 = s1[1:]
                s2 = s2[1:]
            else:
                break
        return res
