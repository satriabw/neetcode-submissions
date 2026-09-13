class Solution:
    def decodeString(self, s: str) -> str:
        # If i seen number we can parse k[char => put it in the stack, mapping using hashmap 
        i = 0
        numStack = []
        charStack = []
        curr = ""
        while i < len(s):
            if s[i] == "]":
                curr = charStack.pop() + (curr * numStack.pop())
                i += 1
            elif not s[i].isdigit():
                curr += s[i]
                i += 1
                continue
            else:
                dig = 0
                while i < len(s) - 1 and s[i].isdigit():
                    dig = (dig*10) + int(s[i])
                    i += 1
                if s[i] == "[":
                    charStack.append(curr)
                    numStack.append(dig)
                    curr = ""
                i += 1
        return curr