from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        result = []

        cols = set()
        posDig = set()
        negDig = set()

        board = [["."]*n for _ in range(n)]

        def backtrack(r: int):

            if r == n:
                copy_board = ["".join(raw) for raw in board]
                result.append(copy_board)
                return

            for c in range(n):
                if c in cols or (r+c) in posDig or (r-c) in negDig:
                    continue

                cols.add(c)
                posDig.add(r+c)
                negDig.add(r-c)
                board[r][c] = "Q"

                backtrack(r+1)

                cols.remove(c)
                posDig.remove(r+c)
                negDig.remove(r-c)
                board[r][c] = "."

        backtrack(0)

        return result