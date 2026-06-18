from typing import List 

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited= set()

        def dfs(node: int, parent: int) -> bool:

            visited.add(node)

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue

                if neighbor in visited:
                    return False

                if not dfs(neighbor, node):
                    return False

            return True

        if not dfs(0, -1):
            return False

        return len(visited) == n