class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Create freq map of the first string
        # Then we do sliding windows by checking the frequency
        # We found valid if such substring exists with same length and freq 0
        freq1 = {}
        for c1 in s1:
            freq1.setdefault(c1, 0)
            freq1[c1] += 1
        
        freq2 = {}
        i, j = 0, 0
        while j < len(s2):
            # Set freq map nya s2
            freq2.setdefault(s2[j], 0)
            freq2[s2[j]] += 1

            # Cari substring sepanjang s1 dulu, lalu cek freqnya sama ga?
            if len(s2[i:j+1]) == len(s1) and all(freq2.get(key, float('-inf')) == freq1[key] for key in freq1):
                return True
            elif len(s2[i:j+1]) == len(s1):
                # Move i and j
                freq2[s2[i]] -= 1
                i += 1
                j += 1
            else:
                j += 1
    
        return False
