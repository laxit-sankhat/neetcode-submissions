from _heapq import heappush
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

from typing import List
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        if not intervals:
            return 0

        intervals.sort(key=lambda interval: interval.start)

        min_heap = []
        max_rooms = 0

        for interval in intervals:
            start = interval.start
            end = interval.end

            while min_heap and min_heap[0] <= start:
                heapq.heappop(min_heap)

            heapq.heappush(min_heap, end)

            max_rooms = max(max_rooms, len(min_heap))

        return max_rooms



