class TimeMap:

    def __init__(self):
        self._map = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self._map.setdefault(key, [])
        self._map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self._map:
            return ""
        lo, hi = 0, len(self._map[key]) - 1
        arr = self._map[key]
        ret = ""

        while lo <= hi:
            mid = (lo + hi) // 2

            if arr[mid][1] > timestamp:
                hi = mid - 1
            else:
                ret = arr[mid][0]
                lo = mid + 1

        return ret


