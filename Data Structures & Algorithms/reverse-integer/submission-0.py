class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1   # 2147483647
        INT_MIN = -2**31      # -2147483648
        result = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            digit = x % 10
            x //= 10
            if result > INT_MAX // 10 or result < INT_MIN // 10:
                return 0
            result = result * 10 + digit
        
        return result * sign
