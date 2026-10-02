class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # i is number banana in pile
        # k is number of hours i have to eat all bananas
        # banana hour per hour rating k
        # find between len(piles) = crates is minimum hour

        def calculateHours(piles, k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
            return hours
                
        lo, hi = max(sum(piles)//h,1), max(piles)
        while lo <= hi:
            if lo >= hi:
                break
            mid = (lo + hi) // 2
            if calculateHours(piles, mid) <= h:
                hi = mid
            else:
                lo = mid + 1
        return lo
    
