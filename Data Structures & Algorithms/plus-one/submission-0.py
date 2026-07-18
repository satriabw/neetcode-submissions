class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []

        remainder = 1
        for digit in reversed(digits):
            d = (digit + remainder) % 10
            remainder = (digit + remainder) // 10

            res.append(d)
        
        if remainder > 0:
            res.append(remainder)

        return res[::-1]