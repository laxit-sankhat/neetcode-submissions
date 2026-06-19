from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        two_step_back = 0
        one_step_back = 0

        for i in range(2, len(cost) + 1):

            current = min(
                one_step_back + cost[i-1],
                two_step_back + cost[i-2]
            )

            two_step_back = one_step_back
            one_step_back = current

        return one_step_back
        