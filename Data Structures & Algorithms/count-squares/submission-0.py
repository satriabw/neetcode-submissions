class CountSquares:

    def __init__(self):
        self._freq = defaultdict(int)
        
    def add(self, point: List[int]) -> None:
        self._freq[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        count = 0
        x1, y1 = point[0], point[1]
        for (x2, y2), freq in self._freq.items():
            if abs(x2-x1) == abs(y2-y1) and x2 != x1 and y2 != y1:
                count += (self._freq.get((x2, y1), 0) * self._freq.get((x1, y2), 0) * self._freq.get((x2, y2), 0))
        
        return count