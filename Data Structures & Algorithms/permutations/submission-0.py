class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        path = []
        used = set()

        def dfs():

            if len(path) == len(nums):
                result.append(path.copy())
                return

            for num in nums:

                if num in used:
                    continue

                path.append(num)
                used.add(num)

                dfs()

                path.pop()
                used.remove(num)

        dfs()
        return result