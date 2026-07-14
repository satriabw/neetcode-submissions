class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # So algorithm works like this
        # For each letter we assume if we dont find different letter in between it is a substring
        
        # Algorithm we will have a set
        # If we find occurence of same string again in the set we will merge all current substring
        last = {}
        for i, c in enumerate(s):
            last[c] = i

        start = 0
        end = 0
        res = []
        for i, c in enumerate(s):
            end = max(end, last[c])
            if i == end:
                res.append(end - start + 1)
                start = i + 1

        return res