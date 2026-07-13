from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda interval: interval[0])

        remove_count = 0
        previous_end = intervals[0][1]

        for start, end in intervals[1:]:
            
            if start < previous_end:
                remove_count += 1

                previous_end = min(previous_end, end)

            else:
                previous_end = end 

        return remove_count