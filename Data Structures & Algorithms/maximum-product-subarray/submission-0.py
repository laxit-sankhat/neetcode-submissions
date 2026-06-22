from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_max = nums[0]
        current_min = nums[0]
        result = nums[0]

        for num in nums[1:]:
            previous_max = current_max
            previous_min = current_min

            current_max = max(
                num,
                num * previous_max,
                num * previous_min
            )

            current_min = min(
                num,
                num * previous_max,
                num * previous_min
            )

            result = max(result, current_max)

        return result