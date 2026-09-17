class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        n = len(points)

        min_dist = [float('inf')] * n
        visited = [False] * n

        min_dist[0] = 0

        total_cost = 0

        for _ in range(n):

            current = -1

            for i in range(n):
                if not visited[i] and (current == -1 or min_dist[i] < min_dist[current]):
                    current = i

            visited[current] = True
            total_cost += min_dist[current]

            x1, y1 = points[current]

            for i in range(n):

                if not visited[i]:
                    x2, y2 = points[i]

                    cost = abs(x1-x2) + abs(y1-y2)

                    if cost < min_dist[i]:
                        min_dist[i] = cost

        return total_cost
