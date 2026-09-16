import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # Build adjacency list
        graph = [[] for _ in range(n + 1)]

        for u, v, t in times:
            graph[u].append((v, t))

        # Shortest distances
        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        # Min heap: (distance, node)
        heap = [(0, k)]

        # Dijkstra
        while heap:
            current_dist, node = heapq.heappop(heap)

            # Skip outdated entry
            if current_dist > dist[node]:
                continue

            for neighbor, weight in graph[node]:

                new_dist = current_dist + weight

                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(heap, (new_dist, neighbor))

        # If any node is unreachable
        if float('inf') in dist[1:]:
            return -1

        # Time when the last node receives signal
        return max(dist[1:])