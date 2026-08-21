class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        n = len(s)

        self._backtrack(s, 0, n, [], result)
        return result


    def _backtrack(self, s: str, start: int, n: int, currPartition: List[str], result: List[List[str]]):
        if start == n:
            result.append(currPartition.copy())
            return
        
        for end in range(start+1, n+1):
            partition = s[start:end]
            if not self._checkPalindrome(partition):
                continue
            currPartition.append(partition)
            self._backtrack(s, end, n, currPartition, result)
            currPartition.pop()
        
    def _checkPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i <= j and s[i] == s[j]:
            i += 1
            j -=1
        return i > j
