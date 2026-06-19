from collections import deque
from typing import List


class Solution:
    def ladderLength(
        self,
        beginWord: str,
        endWord: str,
        wordList: List[str]
    ) -> int:

        words = set(wordList)

        if endWord not in words:
            return 0

        queue = deque([(beginWord, 1)])

        words.discard(beginWord)

        while queue:
            current_word, sequence_length = queue.popleft()

            if current_word == endWord:
                return sequence_length

            chars = list(current_word)

            for i in range(len(chars)):
                original_char = chars[i]

                for code in range(ord("a"), ord("z") + 1):
                    new_char = chr(code)

                    if new_char == original_char:
                        continue

                    chars[i] = new_char
                    next_word = "".join(chars)

                    if next_word in words:
                        words.remove(next_word)

                        queue.append(
                            (next_word, sequence_length + 1)
                        )

                chars[i] = original_char

        return 0