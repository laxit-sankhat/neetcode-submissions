"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

from typing import List


class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Sort meetings according to starting time
        intervals.sort(key=lambda interval: interval.start)

        # Check consecutive meetings for overlap
        for i in range(1, len(intervals)):
            previous = intervals[i - 1]
            current = intervals[i]

            if current.start < previous.end:
                return False

        return True