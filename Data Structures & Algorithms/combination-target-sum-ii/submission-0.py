class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()

        result = []
        path = []

        def dfs(start, remaining):
            if remaining == 0:
                result.append(path.copy())
                return

            if remaining < 0:
                return

            for i in range(start, len(candidates)):

                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                if candidates[i] > remaining:
                    break

                path.append(candidates[i])

                dfs(i + 1, remaining - candidates[i])

                path.pop()

        dfs(0, target)
        return result