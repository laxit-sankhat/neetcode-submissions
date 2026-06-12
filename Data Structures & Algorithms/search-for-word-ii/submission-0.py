class Trienode:
    def __init__(self) -> None:
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = Trienode()

        for word in words:
            curr = root 

            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = Trienode()

                curr = curr.children[ch]

            curr.word = word

        rows = len(board)
        cols = len(board[0])
        result = set()

        def dfs(r, c, node):

            if(
                r<0 or r>=rows or
                c<0 or c>= cols
            ):
                return

            ch = board[r][c]

            if ch == "#" or ch not in node.children:
                return

            node = node.children[ch]

            if node.word:
                result.add(node.word)

            board[r][c] = "#"

            dfs(r+1, c, node)
            dfs(r-1, c, node)
            dfs(r, c+1, node)
            dfs(r, c-1, node)

            board[r][c] = ch

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return list(result)