from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        freq = Counter(tasks)

        max_freq = max(freq.values())

        countMaxFreq = 0

        for count in freq.values():
            if count == max_freq:
                countMaxFreq += 1

        formula = (max_freq - 1) * (n + 1) + countMaxFreq

        return max(len(tasks), formula)