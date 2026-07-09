from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        result = []

        for i in range(len(intervals)):
            current_start = intervals[i][0]
            current_end = intervals[i][1]

            new_start = newInterval[0]
            new_end = newInterval[1]

            if new_end < current_start:
                result.append(newInterval)
                return result + intervals[i:]

            elif current_end < new_start:
                result.append(intervals[i])

            else:
                newInterval[0] = min(new_start, current_start)
                newInterval[1] = max(new_end, current_end)

        result.append(newInterval)

        return result