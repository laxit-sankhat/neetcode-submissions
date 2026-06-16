class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0

        def dfs(r: int, c: int) -> int:
            # Boundary or water check
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == 0
            ):
                return 0

            # Mark visited
            grid[r][c] = 0

            # Count current cell + connected land
            area = 1
            area += dfs(r + 1, c)  # down
            area += dfs(r - 1, c)  # up
            area += dfs(r, c + 1)  # right
            area += dfs(r, c - 1)  # left

            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    island_area = dfs(r, c)
                    max_area = max(max_area, island_area)

        return max_area