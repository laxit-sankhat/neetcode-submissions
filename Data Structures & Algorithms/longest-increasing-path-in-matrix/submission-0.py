from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        rows = len(matrix)
        cols = len(matrix[0])

        memo = [[0] * cols for _ in range(rows)]

        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),
        ] 

        def dfs(row: int, col: int) -> int:

            if memo[row][col] != 0:
                return memo[row][col]

            longest = 1 

            for dr, dc in directions:
                next_row = row + dr
                next_col = col + dc

                inside_grid = (
                    0 <= next_row < rows
                    and 0 <= next_col < cols
                )

                if(
                    inside_grid and matrix[next_row][next_col] > matrix[row][col]
                ):
                    longest = max(longest, 1 + dfs(next_row, next_col))

                memo[row][col] = longest

            return longest

        answer = 0

        for row in range(rows):
            for col in range(cols):
                answer = max(answer, dfs(row, col))

        return answer
