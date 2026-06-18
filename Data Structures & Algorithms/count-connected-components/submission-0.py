from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        components = 0

        for node in range(n):
            if node in visited:
                continue

            components += 1

            stack = [node]
            visited.add(node)

            while stack:
                current = stack.pop()

                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)

        return components

