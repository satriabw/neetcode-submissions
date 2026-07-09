class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        
        for string in strs:
            encoded += str(len(string))
            encoded += '#'
            encoded += string
        
        return encoded

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while (i < len(s)):
            flag = ''
            while i < len(s) and s[i] != '#':
                flag += s[i]
                i += 1

            # get length flag
            length = int(flag)
            i += 1

            strs.append(s[i:i+length])
            
            i += length
        
        return strs
