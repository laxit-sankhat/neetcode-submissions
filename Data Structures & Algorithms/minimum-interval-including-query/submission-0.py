from typing import List
import heapq


class Solution:
    def minInterval(
        self,
        intervals: List[List[int]],
        queries: List[int]
    ) -> List[int]:
        intervals.sort()

        sorted_queries = sorted(
            (query, index)
            for index, query in enumerate(queries)
        )

        answer = [-1] * len(queries)

        min_heap = [] 
        i = 0

        for query, original_index in sorted_queries:

            while i < len(intervals) and intervals[i][0] <= query:
                left, right = intervals[i]
                length = right - left + 1

                heapq.heappush(min_heap, (length, right))
                i += 1

            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)

            if min_heap:
                answer[original_index] = min_heap[0][0]

        return answer