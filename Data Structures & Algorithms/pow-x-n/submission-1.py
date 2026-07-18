class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        if n == 0:
            return 1
        y = 1
        while n > 1:
            if n % 2 == 1:
                y = x * y
                n = n - 1
            x = x * x
            n = n/2

        return x * y