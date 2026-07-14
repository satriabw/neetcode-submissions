class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # So algorithm works like this
        # For each letter we assume if we dont find different letter in between it is a substring
        
        # Algorithm we will have a set
        # If we find occurence of same string again in the set we will merge all current substring
        occ = {}
        for i, word in enumerate(s):
            # merge the substring
            if word in occ:
                occ[word][1] = i
            else:
                occ.setdefault(word, [])
                occ[word].append(i)
                occ[word].append(i)
        
        curr_start = float('inf')
        curr_end = float('inf')
        res = []

        for key, val in occ.items():
            if curr_start == float('inf') and curr_end == float('inf'):
                curr_start = val[0]
                curr_end = val[1]
            else:
                if val[0] > curr_start and val[0] < curr_end:
                    curr_end = max(curr_end, val[1])
                # start of new string
                elif val[0] > curr_end:
                    res.append(curr_end-curr_start+1)
                    curr_start =  val[0]
                    curr_end = val[1]

        res.append(curr_end-curr_start+1)
        return res