class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        result = []
        path = []

        def dfs(index, remaining):
            if remaining == 0:
                result.append(path.copy())
                return

            if remaining < 0 or index == len(nums):
                return

            path.append(nums[index])
            dfs(index, remaining - nums[index])

            path.pop()

            dfs(index + 1, remaining)

        dfs(0, target)

        return result