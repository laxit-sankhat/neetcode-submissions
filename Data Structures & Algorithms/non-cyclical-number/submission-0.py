class Solution:
    def isHappy(self, n: int) -> bool:

        def sum_square_digits(n):
            total = 0

            while n > 0:
                digit = n % 10
                total += digit * digit
                n //= 10

            return total

        seen = set()

        while n != 1:
            if n in seen:
                return False

            seen.add(n)
            n = sum_square_digits(n)

        return True