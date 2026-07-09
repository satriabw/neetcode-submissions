class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 0
        freq = {}
        res = 0

        i, j = 0, 0
        while i <= j and i < len(s):
            while j < len(s):
                freq.setdefault(s[j], 0)
                freq[s[j]] += 1
                max_freq = max(max_freq, freq[s[j]])
                j += 1

                if len(s[i:j]) - max_freq > k:
                    break

                res = len(s[i:j])

            freq[s[i]] -= 1

            i += 1

        return res

            