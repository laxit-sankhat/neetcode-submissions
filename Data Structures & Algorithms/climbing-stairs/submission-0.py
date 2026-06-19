class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        two_step_back = 1
        one_step_back = 2

        for step in range(3, n+1):
            current = one_step_back + two_step_back

            two_step_back = one_step_back
            one_step_back = current

        return one_step_back