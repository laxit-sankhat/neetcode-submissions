class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        if num1 == "0" or num2 == "0":
            return "0"

        m = len(num1)
        n = len(num2)

        res = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')

                product = digit1 * digit2

                p1 = i + j
                p2 = i + j + 1

                total = product + res[p2]

                res[p2] = total % 10
                res[p1] += total // 10

        while res[0] == 0:
            res.pop(0)

        return ''.join(map(str, res))