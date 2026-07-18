class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        val = n
        while val != 1:
            if val in seen:
                return False
            
            total = 0
            digits = str(val)
            for digit in digits:
                total += (int(digit)**2)

            val = total
            if val < 10:
                seen.add(val)

        return True