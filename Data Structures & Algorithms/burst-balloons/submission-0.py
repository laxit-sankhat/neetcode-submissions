from functools import cache
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        values = [1] + nums + [1]
        n = len(values)

        @cache
        def dfs(left: int, right: int) -> int:
            if left + 1 == right:
                return 0

            best = 0

            for k in range(left + 1, right):
                coins = (
                    dfs(left, k)
                    + values[left] * values[k] * values[right]
                    + dfs(k, right)
                )

                best = max(best, coins)

            return best

        return dfs(0, n - 1)