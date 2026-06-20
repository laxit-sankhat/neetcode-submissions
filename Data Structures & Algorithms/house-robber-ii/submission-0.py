from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)

        if n== 1:
            return nums[0]

        def rob_linear(start: int, end: int) -> int:

            two_back = 0
            one_back = 0

            for i in range(start, end+1):

                current = max(
                    one_back, two_back + nums[i]
                )

                two_back = one_back
                one_back = current

            return one_back

        case1 = rob_linear(0, n-2)
        case2 = rob_linear(1, n-1)

        return max(case1, case2)