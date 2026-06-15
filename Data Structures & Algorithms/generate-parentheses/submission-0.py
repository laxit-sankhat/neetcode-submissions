from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []

        def backtrack(path: str, open_count: int, close_count: int):

            if len(path) == 2*n:
                result.append(path)
                return

            if open_count < n:
                backtrack(path + "(", open_count + 1, close_count)

            if close_count < open_count:
                backtrack(path + ")", open_count, close_count + 1)

        backtrack("", 0, 0)

        return result 