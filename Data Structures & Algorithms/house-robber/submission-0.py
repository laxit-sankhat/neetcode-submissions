from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        two_houses_back = 0
        one_house_back = 0

        for money in nums:
            current = max(
                one_house_back,         
                money + two_houses_back  
            )

            two_houses_back = one_house_back
            one_house_back = current

        return one_house_back