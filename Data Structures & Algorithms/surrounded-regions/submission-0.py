from collections import deque
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        queue = deque()

        def add_safe_cell(r: int, c: int) -> None:
            if board[r][c] == "O":
                board[r][c] = "T"
                queue.append((r, c))


        for r in range(rows):
            add_safe_cell(r, 0)
            add_safe_cell(r, cols - 1)

        for c in range(cols):
            add_safe_cell(0, c)
            add_safe_cell(rows - 1, c)

        directions = [
            (1, 0),   
            (-1, 0),
            (0, 1),   
            (0, -1)   
        ]

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and board[nr][nc] == "O"
                ):
                    board[nr][nc] = "T"
                    queue.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"