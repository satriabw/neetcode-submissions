class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        self._helper(n, k, 1, [], results)
        return results
    

    def _helper(self, n: int, k: int, start: int, current: List[int], results: List[List[int]]):
        if len(current) == k:
            results.append(current.copy())
            return

        for i in range(start, n+1):
            current.append(i)
            self._helper(n, k, i+1, current, results)
            current.pop()
