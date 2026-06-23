from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        max_word_length = max(len(word) for word in wordDict)

        n = len(s)

        dp = [False] * (n + 1)
        dp[0] = True

        for end in range(1, n + 1):
            earliest_start = max(0, end - max_word_length)

            for start in range(earliest_start, end):
                if dp[start] and s[start:end] in word_set:
                    dp[end] = True
                    break

        return dp[n]