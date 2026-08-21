class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lo = max(weights)
        hi = sum(weights)
        return self.searchCapacity(lo, hi, weights, days)
    

    def searchCapacity(self, lo: int, hi: int, weights: List[int], days: int) -> int:
        if lo == hi:
            return lo

        capacity = (lo+hi) // 2
        daysNeeded = self.countDaysNeeded(weights, capacity)

        if daysNeeded > days:
            return self.searchCapacity(capacity+1, hi, weights, days)
        else:
            return self.searchCapacity(lo, capacity, weights, days)
    
    def countDaysNeeded(self, weights: List[int], capacity: int) -> int:
        days = 1

        curr = 0
        for weight in weights:
            curr += weight
            if curr > capacity:
                days += 1
                curr = weight
        
        return days