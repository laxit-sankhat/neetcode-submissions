from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def dfs(r: int, c: int, index: int):

            if index == len(word):
                return True

            if(
                r < 0 or r >= rows or c < 0 or c >= cols or
                board[r][c] != word[index] or 
                (r,c) in visited 
            ):
                return False

            visited.add((r,c))

            found = (
                dfs(r+1, c, index+1) or
                dfs(r-1, c, index+1) or
                dfs(r, c+1, index+1) or
                dfs(r, c-1, index+1)
            )

            visited.remove((r,c))

            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False

