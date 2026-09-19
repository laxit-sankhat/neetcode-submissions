import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        n = len(grid)

        time =  [[float('inf')] * n for _ in range(n)]

        time[0][0] = grid[0][0]

        heap = [(grid[0][0], 0, 0)]

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while heap:

            currnt_time, r, c = heapq.heappop(heap)

            if(r, c) == (n-1, n-1):
                return currnt_time

            if currnt_time > time[r][c]:
                continue

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                if 0 <= nr < n and 0 <= nc < n:

                    new_time = max(currnt_time, grid[nr][nc])

                    if new_time < time[nr][nc]:
                        time[nr][nc] = new_time

                        heapq.heappush(heap, (new_time, nr, nc))