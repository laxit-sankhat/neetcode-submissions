from functools import cache
from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @cache
        def dfs(index: int, current_total: int) -> int:

            if index == len(nums):
                return 1 if current_total == target else 0

            add = dfs(index + 1, current_total + nums[index])
            subtract = dfs(index + 1, current_total - nums[index])

            return add + subtract

        return dfs(0, 0)