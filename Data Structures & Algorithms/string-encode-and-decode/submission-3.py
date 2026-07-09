class Solution:
    # Solutions is to have helper character as a first character
    # We can encode then what is the length of the each char like
    # #5=> length of word
    # H1 => H
    # e1 => e
    # l2 => ll
    # o1 => o

    # 1 + 1 + 2 + 1 = 5 => next is new charcters 

    def encode(self, strs: List[str]) -> str:
        delim = "#"
        encoded = ''

        for s in strs:
            encoded += str(len(s)) + delim
            encoded += s

        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        j = 0

        while i < len(s):
            # Get character length
            while s[j] != '#' and s[j].isdigit(): j += 1
            char_len = int(s[i:j])
            result.append(s[j+1:j+1+char_len])
            i = j + 1 + char_len
            j = i

        return result