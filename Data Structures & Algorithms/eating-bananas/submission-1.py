class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        # Binary search idea
        # Find for 1...max(p)
        # Start from mid, if we can get all banans < h then to the left else increase
        return self.search(piles, h, 1, max(piles), max(piles))


    def search(self, piles, h, low, hi, k):
        if low >= hi:
            if self.check(piles, low, h):
                return low
            else:
                return k
        
        mid = (low+hi) // 2

        if self.check(piles, mid, h):
            return self.search(piles, h, low, mid, mid)
        else:
            return self.search(piles, h, mid+1, hi, k)

    def check(self, piles, k, h):
        curr = 0
        for pile in piles:
            curr += math.ceil(pile/k)
            if curr > h:
                return False
        return True
