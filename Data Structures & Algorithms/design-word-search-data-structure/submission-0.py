class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()


    def addWord(self, word: str) -> None:

        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()

            curr = curr.children[ch]

        curr.endOfWord = True


    def search(self, word: str) -> bool:

        def dfs(index, node):

            curr = node

            for i in range(index, len(word)):

                ch = word[i]

                if ch == ".":

                    for child in curr.children.values():

                        if dfs(i + 1, child):
                            return True

                    return False

                else:

                    if ch not in curr.children:
                        return False

                    curr = curr.children[ch]

            return curr.endOfWord

        return dfs(0, self.root)