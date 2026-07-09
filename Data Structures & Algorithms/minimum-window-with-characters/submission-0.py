class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Ideanya sederhana, pake freq map match => pastiin t exists in substring s
        # Expand terus jnya, nanti pelan2 kecilin i sampe minimum aja
        # di return kalau udah dapet minimum 
        if len(t) > len(s):
            return ""

        # Frequency of t
        freqt = {}
        for c in t:
            freqt.setdefault(c, 0)
            freqt[c] += 1
        
        res = (0, 0)
        min_len = float('inf')
        
        freqs = {}
        i, j = 0, 0
        while j < len(s):
            freqs.setdefault(s[j], 0)
            freqs[s[j]] += 1

            # cek buat dapet minimal
            while len(s[i:j+1]) >= len(t) and all(freqs.get(k, -999) >= freqt[k] for k in freqt):
                if j+1-i <= min_len:
                    res = (i, j+1)
                    min_len = j+1-i
                    
                freqs[s[i]] -= 1
                i += 1

            # Expand until len s[i:j+1] >= s
            j += 1

        return s[res[0]:res[1]]